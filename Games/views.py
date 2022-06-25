from django.shortcuts import render
from django.views import View


# Create your views here.

class RockScissorsPaperView(View):
    template_name = "RockScissorsPaper/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
