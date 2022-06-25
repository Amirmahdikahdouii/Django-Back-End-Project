from django.urls import path
from .views import RockScissorsPaperView

urlpatterns = [
    path("rock-scissors-paper/", RockScissorsPaperView.as_view(), name="rockScissorsPaperView"),
]
