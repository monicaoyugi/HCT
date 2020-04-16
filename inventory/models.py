from django.db import models
from authentication.models import User


# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=15)
    hospital_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Donor(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20)
    hospital = models.ForeignKey(Hospital, null=True, on_delete=models.CASCADE)


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
