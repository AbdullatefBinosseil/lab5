from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

class PersonForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

def add(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            new_person = Person(username, password)
            people.append(new_person)
            return HttpResponseRedirect(reverse("theApp:index"))
    else:
        form = PersonForm()

    return render(request, "theApp/add.html", {"form": form})

def index(request):
    return render(request, "theApp/index.html", {"people": people})