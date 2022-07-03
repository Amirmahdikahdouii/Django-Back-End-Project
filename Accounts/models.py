from django.db import models
from django.contrib.auth.models import User
from .utils.changeImageName import changeProfilePictureName


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    mobile = models.CharField(max_length=12, verbose_name="Mobile Number")
    bio = models.CharField(max_length=1200, null=True, blank=True, verbose_name="Bio")
    birthday = models.DateField(verbose_name="BirthDay")
    profile_picture = models.ImageField(upload_to=changeProfilePictureName, verbose_name="Image")
    blog_writer = models.BooleanField(default=False, verbose_name="Blog Writer")

    def __str__(self):
        return f"{self.id}-{self.user.username}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
