from django.shortcuts import render, redirect
from django.views import View


class HomePage(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
