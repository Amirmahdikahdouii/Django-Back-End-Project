from django.urls import path
from . import views

urlpatterns = [
    path("", views.MiniProjectsView.as_view(), name="miniProjectsView"),
    path('calculator/', views.MiniProjectsCalculatorView.as_view(), name="miniProjectsCalculator"),
]
