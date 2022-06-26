from django.shortcuts import render
from django.views import View
from .models import RockScissorsPaper


# Create your views here.

class RockScissorsPaperView(View):
    template_name = "RockScissorsPaper/index.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, self.template_name, {})
        user = request.user
        context = {"user": user.username, "win": 0, "lose": 0}
        try:
            userModel = RockScissorsPaper.objects.get(user=user)
        except RockScissorsPaper.DoesNotExist:
            return render(request, self.template_name, context)
        context["win"] = userModel.winCount
        context["lose"] = userModel.loseCount
        return render(request, self.template_name, context)


class RockScissorsPaperSaveData(View):
    def get(self, request, *args, **kwargs):
        from django.http import JsonResponse
        responseData = {
            "userAuthenticated": False,
            "statusCode": None,
            "winCount": 0,
            "loseCount": 0,
        }
        if not request.user.is_authenticated:
            return JsonResponse(responseData)
        responseData["userAuthenticated"] = True
        statusCode = kwargs.get("statusCode", None)
        if statusCode is None:
            return JsonResponse(responseData)
        statusCode = int(statusCode)
        statusCodes = [1, 2]
        if statusCode not in statusCodes:
            responseData["statusCode"] = False
            return JsonResponse(responseData)
        responseData["statusCode"] = statusCode
        user = request.user
        try:
            modelsInstance = RockScissorsPaper.objects.get(user=user)
        except RockScissorsPaper.DoesNotExist:
            modelsInstance = RockScissorsPaper()
            modelsInstance.user = user
        if statusCode == 1:
            modelsInstance.winCount += 1
        elif statusCode == 2:
            modelsInstance.loseCount += 1
        modelsInstance.save()
        responseData["winCount"] = modelsInstance.winCount
        responseData["loseCount"] = modelsInstance.loseCount
        return JsonResponse(responseData)
