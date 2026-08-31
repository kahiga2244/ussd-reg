from django.contrib.auth.hashers import make_password
from .models import User
import secrets


def user_exists(phone):

    return User.objects.filter(
        phone_number=phone
    ).exists()


def id_exists(id_number):

    return User.objects.filter(
        id_number=id_number
    ).exists()


def email_exists(email):

    return User.objects.filter(
        email=email
    ).exists()


def generate_ardhisasa_id():

    while True:

        number = secrets.randbelow(
            90000000
        ) + 10000000

        ardhisasa_id = f"ARD{number}"

        if not User.objects.filter(
            ardhisasa_id=ardhisasa_id
        ).exists():

            return ardhisasa_id


def register_user(data):

    ardhisasa_id = generate_ardhisasa_id()

    user = User.objects.create(

        ardhisasa_id=ardhisasa_id,

        id_type=data["id_type"],

        id_number=data["id_number"],

        phone_number=data["phone"],

        email=data["email"],

        password=make_password(
            data["password"]
        )

    )

    return user