from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Validations is only with Username and Username Fill with Email Of User
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


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


# TODO: make change User Password Form
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "change-personal-info-form-input",
        }), required=True, empty_value=False, max_length=250, label="Old Password: "
    )

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "change-personal-info-form-input",
        }), required=True, empty_value=False, max_length=250, label="New Password: ",
        validators=[
            validators.MaxLengthValidator(limit_value=250, message="Please Enter Less than 250 characters"),
            validators.MinLengthValidator(limit_value=5, message="Please Enter More than 5 characters"),
        ]
    )

    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "change-personal-info-form-input",
        }), required=True, empty_value=False, max_length=250, label="Confirm New Password: ", min_length=5,
        validators=[
            validators.MaxLengthValidator(limit_value=250, message="Please Enter Less than 250 characters"),
            validators.MinLengthValidator(limit_value=5, message="Please Enter More than 5 characters"),
        ]
    )

    def checkOldPassword(self, username=None):
        oldPasswordValue = self.data.get("old_password", None)
        if oldPasswordValue is None:
            raise forms.ValidationError("Old Password is Empty!")
        try:
            user = User.objects.get(username=username, password=oldPasswordValue)
        except User.DoesNotExist:
            raise forms.ValidationError("Old Password is Not true!")
        return user, oldPasswordValue

    def checkNewPasswordAndConfirmField(self):
        newPassword = self.data.get("new_password", None)
        confirmNewPassword = self.data.get("confirm_new_password", None)
        if (newPassword is None) | (confirmNewPassword is None):
            raise forms.ValidationError("The New Password Fields Shouldn't Be Empty")
        if newPassword != confirmNewPassword:
            raise forms.ValidationError("The New Password Field and Confirm password Fields are not match together")
        return newPassword

    def changeNewPassword(self, userObject: User, newPassword: str, oldPassword: str):
        if oldPassword == newPassword:
            raise forms.ValidationError("The New Password and Old password cannot be the same")
        userObject.password = newPassword
        userObject.save()
        return True


# TODO: make Form For get Full data from user
class ProfileConfirmPersonalInfo(forms.Form):
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "change-personal-info-form-input",
        }), required=True, max_length=12, empty_value=False, validators=[
            validators.MaxLengthValidator(limit_value=12, message="Max Length for Phone Number is 12 character!")
        ], label="Mobile: "
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "change-personal-info-form-input",
            "id": "user-bio-textarea"
        }), required=True, max_length=1200, empty_value=False, validators=[
            validators.MaxLengthValidator(limit_value=1200, message="Max Length for Bio is 1200 character!")
        ], label="Bio: "
    )
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={
            "class": "change-personal-info-form-input",
            "placeholder": "Year/ Month/ Day"
        }), required=True, label="Birthday: "
    )
    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "change-personal-info-form-input",
        }), required=True, allow_empty_file=False, label="Profile Image",
    )
