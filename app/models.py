from django.db import models

class User(models.Model):
    ID_TYPES = [
        ("NATIONAL", "National ID"),
        ("ALIEN", "Alien ID"),
        ("MAISHA", "Maisha ID"),
    ]

    id_type = models.CharField(max_length=20, choices=ID_TYPES)
    id_number = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # store a hashed password
    created_at = models.DateTimeField(auto_now_add=True)




class LandRecord(models.Model):
    county = models.CharField(max_length=100)
    registry = models.CharField(max_length=100)
    plot_number = models.CharField(max_length=100, unique=True)
    owner = models.CharField(max_length=200)