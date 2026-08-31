import re


def valid_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return bool(re.match(pattern, email))


def valid_phone(phone):

    phone = phone.replace("+", "")

    return phone.isdigit() and len(phone) >= 10


def valid_id_number(id_number):
    return id_number.isdigit() and len(id_number) >= 6