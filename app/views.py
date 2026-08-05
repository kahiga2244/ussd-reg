from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .menu import menu

@csrf_exempt
def home(request):
    text = request.POST.get("text", "")
    phone = request.POST.get("phoneNumber")

    response = menu(text, phone)

    return HttpResponse(response, content_type="text/plain")