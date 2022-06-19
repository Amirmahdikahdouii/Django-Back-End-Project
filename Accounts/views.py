from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import RegisterForm
from django.contrib.auth.models import User


# Create your views here.


class SignUpView(CreateView):
    template_name = "account/registerPage.html"
    form_class = RegisterForm
    model = User
