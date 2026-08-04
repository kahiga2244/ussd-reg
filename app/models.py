from django.db import models

class USSDUser(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.phone_number})"
