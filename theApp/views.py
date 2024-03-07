from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
people=[]
# Create your views here.
class person(forms.Form):
    username=forms.CharField(label="username")
    password=forms.CharField(widget=forms.PasswordInput(), label="Password")
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def __str__(self):
        return self.username

def add(request):
    if request.method == "POST" :
        form = person(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            Personn = person(username=username, password=password)
            people.append(Personn)
            return HttpResponseRedirect (reverse("theApp: index"))
        else:
            return render (request, "theApp/add.html",{
                "form":form
            })
    return render(request, "theApp/add.html", {
        "form":person()
    })
def index(request):
    return render(request, "theApp/index.html",{
        "people":people
    })



