from django.shortcuts import render
from reguser.models import Userreg
from reguser.models import EmployeeDetails
from reguser.forms import empforms
from django.contrib import messages
from django.db import connection

#View for User Registration
def Userregistration(request):
    if request.method == 'POST':
        if request.POST.get('uname') and request.POST.get('uemail') and request.POST.get('pwd') and request.POST.get('maritalstatus') and request.POST.get('gender'):
            saverecord=Userreg()
            saverecord.uname = request.POST.get('uname')
            saverecord.uemail = request.POST.get('uemail')
            saverecord.pwd = request.POST.get('pwd')
            saverecord.maritalstatus = request.POST.get('maritalstatus')
            saverecord.gender = request.POST.get('gender')
            saverecord.save()
            messages.success(request,"New User Registration Details Saved Successfully...!")
            return render(request,'Register.html')
    else:
            return render(request,'Register.html')

#View for data insertion
def Insertrecord(request):
    if request.method == 'POST':
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('salary'):
            saverecord=EmployeeDetails()
            saverecord.empname = request.POST.get('empname')
            saverecord.email = request.POST.get('email')
            saverecord.salary = request.POST.get('salary')
            saverecord.save()
            messages.success(request,"Record Saved Successfully...!")
            return render(request,'Insert.html')
    else:
            return render(request,'Insert.html')

#view for displaying data before deletion from MySQL Database
def datadisplay(request):
    result=EmployeeDetails.objects.all()
    return render(request,"Delete.html",{"delemprec":result})

#view for deleting record
def delrec(request,id):
    delemployee=EmployeeDetails.objects.get(id=id)
    delemployee.delete()
    result=EmployeeDetails.objects.all()
    return render(request,"Delete.html",{"delemprec":result})

#View for Fetching Data from MySQL Database
def Showemp(request):
    resultdisplay=EmployeeDetails.objects.all()
    return render(request, "Fetch.html",{'EmployeeDetails':resultdisplay})

#View for Fetching Data from MySQL Stored Procedure Database
def Showdetails(request):
    cursor=connection.cursor()
    cursor.execute("call GetEmployeeRecordsSP('fetch')")
    results=cursor.fetchall()
    return render(request,'FetchSP.html',{'getempdetails':results})


#View for displaying data of all records before Editing Update page
def displaydata(request):
    results = EmployeeDetails.objects.all()
    return render(request,"EditUpdate.html",{"editupdaterecord":results})

#View for displaying page to upate the specific record
def editemp(request,id):
    displayemp=EmployeeDetails.objects.get(id=id)
    return render(request,"Edit.html",{"editupdaterecord":displayemp})

#View for updating records
def updateemp(request,id):
    updateemp=EmployeeDetails.objects.get(id=id)
    form=empforms(request.POST,instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,"Record Updated Successfully...!")
        return render(request,"Edit.html",{"editupdaterecord":updateemp})
