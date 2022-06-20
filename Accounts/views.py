from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


# Create your views here.

def registerPage(req):
    if req.user.is_authenticated:
        return HttpResponse("Profile Page")
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
    else:
        return HttpResponseForbidden(content_type="html", content="Not Access To this page")


def loginPage(req):
    if req.user.is_authenticated:
        return HttpResponse("profile Page")
    if req.method == "POST":
        loginForm = LoginForm(req.POST)
        userNameExist = loginForm.checkUsername()
        if userNameExist is not None:
            return render(req, "account/loginPage.html", {"form": loginForm, "error": userNameExist})
        username = loginForm.data.get("username")
        password = loginForm.data.get("password")

        def getUserModel(userName: str, passWord: str, fieldForUsername):
            if fieldForUsername == "username":
                userModel = User.objects.get(username=userName, password=passWord)
                return userModel
            userModel = User.objects.get(email=userName, password=passWord)
            return userModel

        try:
            user = getUserModel(username, password, "username")
            login(req, user)
            return HttpResponse("profile Page")
        except User.DoesNotExist:
            try:
                user = getUserModel(username, password, "email")
                login(req, user)
                return HttpResponse("profile Page")
            except User.DoesNotExist:
                return render(req, "account/loginPage.html",
                              {"form": loginForm, "error": "Username or Password is Not Valid"})
    elif req.method == "GET":
        loginForm = LoginForm()
        return render(req, "account/loginPage.html", {"form": loginForm})


def logOut(req):
    if req.user.is_authenticated:
        logout(req)
        return redirect("loginPage")
    return HttpResponseForbidden("You Dont Have Access to this URL")
