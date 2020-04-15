from django.db import models
from authentication.models import User
import datetime

# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=15)
    hospital_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Donor(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=64)
    location = models.CharField(max_length=20)
    date = models.DateField(("Date"), default=datetime.date.today)
    User = models.ForeignKey(Hospital, null=True, on_delete=models.CASCADE)


def __str__(self):
    return f'{self.name}'


class ItemDonated(models.Model):
    name = models.CharField(max_length=105)
    serial_number = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    notes = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.name}'
