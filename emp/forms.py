from django import forms
from .models import MyEmp
from django.contrib.auth.forms import UserCreationForm

class EmployeeRegistrationForm(UserCreationForm):
    class Meta:
        model=MyEmp
        fields=["first_name","last_name","email","phone","gender","department","image","dob","doj","address","username","password1","password2"]
        widgets={
        "first_name": forms.TextInput(attrs={"class": "form-control form-label"}),
        "last_name": forms.TextInput(attrs={"class": "form-control form-label"}),
        "email": forms.TextInput(attrs={"class": "form-control form-label"}),
        "phone": forms.TextInput(attrs={"class": "form-control form-label"}),
        "department": forms.TextInput(attrs={"class": "form-control form-label"}),
        "address": forms.Textarea(attrs={"class": "form-control form-label"}),
        "username": forms.TextInput(attrs={"class": "form-control form-label"}),
        "password1": forms.PasswordInput(attrs={"class": "form-control form-label"}),
        "password2": forms.PasswordInput(attrs={"class": "form-control form-label"}),
       }

    def __init__(self, *args, **kwargs):
        super(EmployeeRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ["first_name","last_name","email","phone","gender","department","image","dob","doj","address","username","password1","password2"]:
            self.fields[fieldname].help_text = None

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-label","placeholder":"Enter Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control form-label","placeholder":"Enter Password"}))