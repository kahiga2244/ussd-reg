from django.contrib.auth.hashers import make_password

from .models import User


def user_exists(phone):

    return User.objects.filter(phone_number=phone).exists()


def id_exists(id_number):

    return User.objects.filter(id_number=id_number).exists()


def email_exists(email):

    return User.objects.filter(email=email).exists()


def register_user(data):

    User.objects.create(

        id_type=data["id_type"],

        id_number=data["id_number"],

        phone_number=data["phone"],

        email=data["email"],

        password=make_password(data["password"])

    )