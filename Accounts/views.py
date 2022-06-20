from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import RegisterForm
from django.contrib.auth.models import User


# Create your views here.

def registerPage(req):
    if req.method == "POST":
        registerForm = RegisterForm(req.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data.get("username")
            email = registerForm.cleaned_data.get("email", "")
            password = registerForm.cleaned_data.get("password1")
            first_name = registerForm.cleaned_data.get("first_name", "")
            last_name = registerForm.cleaned_data.get("last_name", "")
            user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect("loginPage")
        return render(req, "account/registerPage.html", {"form": registerForm})
    elif req.method == "GET":
        registerForm = RegisterForm()
        return render(req, "account/registerPage.html", {"form": registerForm})


def login(req):
    return HttpResponse("Hi")
