from django.shortcuts import render
from django.views import View
from .models import MiniProjectsCardList


class MiniProjectsView(View):
    template_name = "miniProjects/index.html"
    model = MiniProjectsCardList

    def get(self, request, *args, **kwargs):
        miniProjectCards = self.model.objects.first()
        context = {"miniProjectCards": miniProjectCards}
        return render(request, self.template_name, context)


class MiniProjectsCalculatorView(View):
    template_name = "miniProjects/calculator.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
