from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import USSDUser

@csrf_exempt
def home(request):
    if request.method != 'POST':
        return HttpResponse("Method not allowed", status=405)

    # Read data from Africa's Talking gateway
    phone_number = request.POST.get("phoneNumber", None)
    text         = request.POST.get("text", "")

    # Split the input text sequence by asterisk to count user steps
    # An empty input text means the user just dialed the USSD code
    input_steps = text.split('*') if text else []
    step_count = len(input_steps)

    # Check if the phone number is already registered in our system
    user_exists = USSDUser.objects.filter(phone_number=phone_number).exists()

    if user_exists:
        response = "END You are already registered in the school database system."
        return HttpResponse(response, content_type='text/plain')

    # Step 0: Initial Screen (User dialed the shortcode)
    if step_count == 0:
        response  = "CON Welcome to School Registration\n"
        response += "1. Register Now\n"
        response += "2. Exit"

    # Step 1: User made an initial choice
    elif step_count == 1:
        if input_steps[0] == '1':
            response = "CON Please enter your full name:"
        elif input_steps[0] == '2':
            response = "END Thank you. Registration cancelled."
        else:
            response = "END Invalid choice. Please try again."

    # Step 2: User provided their name, now ask for their age
    elif step_count == 2:
        name = input_steps[1]
        response = f"CON Thank you {name}.\nHow old are you?"

    # Step 3: User provided their age, save information and finalize registration
    elif step_count == 3:
        name = input_steps[1]
        age_str = input_steps[2]

        try:
            age = int(age_str)
            # Save the new user record into the Django database
            USSDUser.objects.create(
                phone_number=phone_number,
                full_name=name,
                age=age
            )
            response = f"END Registration successful!\nWelcome {name}, you have been registered."
        except ValueError:
            # Handle non-numeric age inputs safely
            response = "END Registration failed. Age must be a valid number. Please dial again."

    else:
        response = "END Invalid input session sequence. Please start over."

    return HttpResponse(response, content_type='text/plain')
