from django.db import models
from django.contrib.auth.models import User
from .utils.changeImageName import changePhotoNameBlogImage, changePhotoNamePostGallery
from django.utils.timezone import now


# Create your models here.

class BlogPost(models.Model):
    writer = models.ForeignKey(User, verbose_name="Writer", on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name="Title")
    content = models.TextField(verbose_name="Post Content", null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True, verbose_name="Post Slug")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    mainImage = models.ImageField(changePhotoNameBlogImage, null=True, blank=True)

    def __str__(self):
        return f"{self.id}.{self.title}"

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name="Post")
    title = models.CharField(max_length=400, verbose_name="Title", null=True, blank=True)
    image = models.ImageField(changePhotoNamePostGallery, null=True, blank=True)

    def __str__(self):
        return f"{self.id}.{self.blog_post.title}"

    class Meta:
        verbose_name = "Blog Post Image"
        verbose_name_plural = "Blog Posts Images"


class BlogPostComment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name="Post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    title = models.CharField(max_length=400, verbose_name="Comment Title")
    content = models.CharField(max_length=10000, verbose_name="Comment Content")
    post_rate = models.PositiveSmallIntegerField(default=3, verbose_name="Rate")
    read_by_admin = models.BooleanField(default=False, verbose_name="Is read")
    date = models.DateField(default=now, verbose_name="Date")

    def __str__(self):
        return f"{self.id}-{self.user.username}"

    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Post Comments"
