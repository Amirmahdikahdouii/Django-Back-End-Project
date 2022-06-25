from django.contrib import admin
from .models import RockScissorsPaper


# Register your models here.
class RockScissorsPaperAdmin(admin.ModelAdmin):
    list_display = [
        "__str__", "winCount", "loseCount"
    ]
    model = RockScissorsPaper


admin.site.register(RockScissorsPaper, RockScissorsPaperAdmin)
