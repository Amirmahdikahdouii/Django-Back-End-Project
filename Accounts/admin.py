from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ["blog_writer"]
    list_display = [
        "__str__", "birthday"
    ]

    sortable_by = ["-id"]

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
