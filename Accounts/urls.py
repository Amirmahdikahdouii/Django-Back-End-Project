from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.registerPage, name="registerPage"),
    path("login/", views.LoginClassView.as_view(), name="loginPage"),
    path("logout/", views.logOut, name="logout"),
]