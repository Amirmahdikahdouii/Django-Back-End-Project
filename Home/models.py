from django.db import models
from .utils.changePictureNameForModel import changePhotoName


# Create your models here.
class HomeCarousel(models.Model):
    title = models.CharField(max_length=500, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    link = models.CharField(max_length=200, verbose_name="Link")
    image = models.ImageField(upload_to=changePhotoName, verbose_name="Image")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    def __str__(self):
        return f"{self.id}-{self.title}"

    class Meta:
        verbose_name = "Home Carousel"
