from django.urls import path
from .views import RockScissorsPaperView, RockScissorsPaperSaveData

urlpatterns = [
    path("rock-scissors-paper/", RockScissorsPaperView.as_view(), name="rockScissorsPaperView"),
    path("rock-scissors-paper/<int:statusCode>/", RockScissorsPaperSaveData.as_view(),
         name="rockScissorsPaperSaveData"),
]
