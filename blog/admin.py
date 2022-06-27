from django.contrib import admin
from .models import BlogPost, BlogPostImage, BlogPostComment


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 'writer', 'title'
    ]
    list_filter = [
        'is_active'
    ]
    sortable_by = ["-id"]

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostAdmin)


class BlogPostImagesAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 'title'
    ]
    sortable_by = ["-id"]

    class Meta:
        model = BlogPostImage


admin.site.register(BlogPostImage, BlogPostImagesAdmin)


class BlogPostCommentsAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 'title', 'read_by_admin', 'date'
    ]
    list_filter = [
        'read_by_admin', 'date'
    ]
    sortable_by = ["-id"]

    class Meta:
        model = BlogPostComment


admin.site.register(BlogPostComment, BlogPostCommentsAdmin)
