# VIEWS
from django.http import JsonResponse
from django.shortcuts import render
from . import wallet

# MAIN
def home(request):
    return render(request=request, template_name="home.html")

def ethereum(request, strength):
    try:
        account = wallet.create(strength=strength)
    except SystemError:
        return JsonResponse(data={"error": "An error has occurred"})
    else:
        return JsonResponse(data=account)
