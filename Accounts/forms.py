from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    fullName = forms.CharField(
        max_length=250, label="Full-Name: ",
        help_text="Please Enter full-Name",
        widget=forms.TextInput(attrs={"class": "register-form-input",
                                      "placeholder": "Full Name"}),
        validators=[
            validators.MaxLengthValidator(message="Username Shouldn't be over 100 character", limit_value=250),
        ]
    )
    email = forms.EmailField(
        required=True, max_length=150, label="E-Mail: ", min_length=8,
        help_text="Please Enter Email",
        widget=forms.EmailInput(attrs={"class": "register-form-input",
                                       "placeholder": "E-Mail"}),
        validators=[
            validators.MaxLengthValidator(message="Email Shouldn't be over 100 character", limit_value=150),
            validators.MinLengthValidator(message="Username Shouldn't be under 5 character", limit_value=8),
            validators.EmailValidator(message="Invalid Email")
        ]
    )
    username = forms.CharField(
        required=True, max_length=100, label="Username: ", min_length=5,
        help_text="Please Enter Username",
        widget=forms.TextInput(attrs={"class": "register-form-input",
                                      "placeholder": "Username"}),
        validators=[
            validators.MaxLengthValidator(message="Username Shouldn't be over 100 character", limit_value=100),
            validators.MinLengthValidator(message="Username Shouldn't be under 5 character", limit_value=5),
            validators.RegexValidator(regex="[A-Za-z][A-Za-z0-9_]{4,99}$", message="Invalid Username")
        ]
    )

    password = forms.CharField(
        required=True, max_length=100, label="Password: ", min_length=8,
        help_text="Please Enter Password",
        widget=forms.PasswordInput(attrs={"class": "register-form-input",
                                          "placeholder": "Password"}),
        validators=[
            validators.MaxLengthValidator(message="Password Shouldn't be over 100 character", limit_value=100),
            validators.MinLengthValidator(message="Password Shouldn't be under 8 character", limit_value=8),
        ]
    )

    re_password = forms.CharField(
        required=True, max_length=100, label="Re-Password: ", min_length=8,
        help_text="Please Enter Password Again",
        widget=forms.PasswordInput(attrs={"class": "register-form-input",
                                          "placeholder": "Re-Password"}),
        validators=[
            validators.MaxLengthValidator(message="Password Shouldn't be over 100 character", limit_value=100),
            validators.MinLengthValidator(message="Password Shouldn't be under 8 character", limit_value=8),
        ]
    )

    def existUsername(self):
        username = self.cleaned_data.get("username")
        result = User.objects.filter(username=username).exists()
        if result:
            raise forms.ValidationError("Username is Already Taken")

    def checkPasswords(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError("Passwords Are Not Match!")
