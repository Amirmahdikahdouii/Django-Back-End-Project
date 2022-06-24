from django.shortcuts import render
from django.views import View
from .models import HomeCarousel


# Create your views here.

class HomeView(View):
    template_name = "index.html"
    model = HomeCarousel

    def get(self, request, *args, **kwargs):
        carouselObjects = self.model.objects.filter(is_active=True)
        return render(request, self.template_name, {"carouselObjects": carouselObjects})
