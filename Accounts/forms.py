from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "register-form-input",
            "placeholder": "Username or Email"
        }), label="Username", min_length=4, max_length=250, help_text="Please FillOut form",
        validators=[
            validators.MinLengthValidator(limit_value=4, message="Username should be at least 4 character"),
            validators.MaxLengthValidator(limit_value=250, message="Username should be maximum 250 character"),
        ], empty_value=False, required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "register-form-input",
            "placeholder": "Password"
        }), label="Password", min_length=4, max_length=250, help_text="Please FillOut form",
        validators=[
            validators.MinLengthValidator(limit_value=4, message="Password should be at least 4 character"),
            validators.MaxLengthValidator(limit_value=250, message="Password should be maximum 250 character"),
        ], empty_value=False, required=True
    )

    def checkUsername(self):
        username = self.data.get("username", None)
        if username is None:
            raise forms.ValidationError("Username Should Not Empty")
        user = User.objects.filter(username=username).first()
        if user is None:
            user = User.objects.filter(email=username).first()
            if user is None:
                return "Username Not Found"
        return None