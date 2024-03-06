from django.shortcuts import render
from django import forms
people=[]
# Create your views here.
class person(forms.Form):
    username=forms.CharField(label="username")
    password=forms.PasswordInput(lable="password")
    def __init__(self,username,password):
        self.username=username
        self.password=password

def add(request):
    return render(request, "theApp/add.html", {
        "form":person()
    })


