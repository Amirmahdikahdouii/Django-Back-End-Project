from django.contrib import admin
from .models import HomeCarousel


# Register your models here.
class HomeCarouselAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']
    ordering = ["-id"]
    list_filter = ['is_active']
    model = HomeCarousel


admin.site.register(HomeCarousel, HomeCarouselAdmin)
