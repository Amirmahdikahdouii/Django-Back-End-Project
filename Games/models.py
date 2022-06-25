from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class RockScissorsPaper(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    winCount = models.IntegerField(default=0, verbose_name="Win")
    loseCount = models.IntegerField(default=0, verbose_name="Lose")

    def __str__(self):
        return f"{self.id}.{self.user.username}"

    class Meta:
        verbose_name = "Rock Scissors Paper"
        verbose_name_plural = "Rock Scissors Paper Table"