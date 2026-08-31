from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .menu import menu


@csrf_exempt
def home(request):

    text = request.POST.get("text", "")
    phone = request.POST.get("phoneNumber", "")

    print("================================")
    print("METHOD:", request.method)
    print("TEXT:", repr(text))
    print("PHONE:", repr(phone))

    try:

        response = menu(text, phone)

        print("RESPONSE:", repr(response))
        print("================================")

        return HttpResponse(
            response,
            content_type="text/plain"
        )

    except Exception as e:

        print("ERROR:", repr(e))
        print("================================")

        raise