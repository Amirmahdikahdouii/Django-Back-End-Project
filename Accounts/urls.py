from django.shortcuts import redirect
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="signupPage"),
    path("login/", views.LoginView.as_view(), name="loginPage"),
    path("profile/", login_required(views.ProfileView.as_view(), login_url="/Account/login/"), name="profilePage"),
    path("profile/game-score/", login_required(views.ProfileGameScoreView.as_view(), login_url="/Account/login/"),
         name="profileGameScore"),
    path("profile/change-password/",
         login_required(views.ProfileChangePasswordView.as_view(), login_url="/Account/login/"),
         name="profileChangePassword"),
    path("logout/", views.logOut, name="logout"),
]
