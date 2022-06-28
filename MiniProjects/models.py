from django.db import models
from .utils.changeImageName import changePhotoNameMiniProjects

# Create your models here.


class MiniProjectsCardList(models.Model):
    name = models.CharField(max_length=500, verbose_name="Project Name")
    path = models.CharField(max_length=500, verbose_name="Slug Path")
    image = models.ImageField(changePhotoNameMiniProjects)
    description = models.CharField(max_length=10000, verbose_name="Description")

    def __str__(self):
        return f"{self.id}-{self.name}"

    class Meta:
        verbose_name = "Mini Project Card"
        verbose_name_plural = "Mini Project Card Lists"
