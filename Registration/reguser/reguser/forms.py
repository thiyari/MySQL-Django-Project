from pyexpat import model
from django import forms
from reguser.models import EmployeeDetails

#using inbuild form properties for updating data
class empforms(forms.ModelForm):
    class Meta:
        model=EmployeeDetails
        fields="__all__"