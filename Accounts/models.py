from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class userProfile(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, verbose_name="User Id")
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Name")