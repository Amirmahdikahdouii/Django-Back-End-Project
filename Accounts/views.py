from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View


# Create your views here.
class SignUpView(View):
    form_class = RegisterForm
    initial = {"key": "value"}
    template_name = "account/accountForm.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse("Profile Page")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email", "")
            password = form.cleaned_data.get("password1")
            first_name = form.cleaned_data.get("first_name", "")
            last_name = form.cleaned_data.get("last_name", "")
            user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect("loginPage")
        return render(request, self.template_name, {"form": form})


class LoginClassView(View):
    form_class = LoginForm
    initial = {"key": "value"}
    template_name = "account/accountForm.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse("profile Page")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        userNameExist = form.checkUsername()
        if userNameExist is not None:
            return render(request, self.template_name, {"form": form, "error": userNameExist})
        username = form.data.get("username")
        password = form.data.get("password")

        def getUserModel(userName: str, passWord: str, fieldForUsername):
            if fieldForUsername == "username":
                userModel = User.objects.get(username=userName, password=passWord)
                return userModel
            userModel = User.objects.get(email=userName, password=passWord)
            return userModel

        try:
            user = getUserModel(username, password, "username")
            login(request, user)
            return HttpResponse("profile Page")
        except User.DoesNotExist:
            try:
                user = getUserModel(username, password, "email")
                login(request, user)
                return HttpResponse("profile Page")
            except User.DoesNotExist:
                return render(request, self.template_name,
                              {"form": form, "error": "Username or Password is Not Valid"})


def logOut(req):
    if req.user.is_authenticated:
        logout(req)
        return redirect("loginPage")
    return HttpResponseForbidden("You Dont Have Access to this URL")


# TODO: Make View For Profile
class ProfileView(View):
    template_name = ""

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
