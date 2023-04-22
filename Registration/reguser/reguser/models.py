from django.db import models

#importing connections package for fetching
from django.db import connections

#user registration helper class
class Userreg(models.Model):
    uname = models.CharField(max_length=100)
    uemail = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    maritalstatus = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    class Meta:
        db_table="newuserreg"

#Fetching data an fetching StoredProcedures, Inserting, Updating and Deletion helper class 
class EmployeeDetails(models.Model):
    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salary = models.IntegerField()
    class Meta:
        db_table="empdetails"

