from django.urls import path
from . import views


urlpatterns = [
    path("sign-up/", views.signUp, name="signupPage"),
    path("login/", views.LoginClassView.as_view(), name="loginPage"),
    path("logout/", views.logOut, name="logout"),
]