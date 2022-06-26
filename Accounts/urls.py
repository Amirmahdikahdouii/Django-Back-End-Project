from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="signupPage"),
    path("login/", views.LoginClassView.as_view(), name="loginPage"),
    path("logout/", views.logOut, name="logout"),
]
