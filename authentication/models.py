from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,
                   first_name=None,
                   last_name=None,
                   username=None,
                   email=None,
                   role='SU',
                   password=None,
                   contact=None,
                   adress=None,
                   ):

        if not first_name:
            raise TypeError("First name is required.")

        if not last_name:
            raise TypeError("Last name is required.")

        if not email:
            raise TypeError("email name is required.")

        if not password:
            raise TypeError("password name is required.")

        if not contact:
                raise TypeError("contact name is required.")

        if not adress:
            raise TypeError("address name is required.")

        user = self.model(first_name=first_name, last_name=last_name,
                        username=username, email=self.normalize_email(email), role='SU')
        user.set_password(password)
        user.is_active = True
        user.is_verified = False
        user.save()

    def create_superuser(self,
                    first_name=None,
                    last_name=None,
                    username=None,
                    email=None,
                    role='HL',
                    password=None,
                    contact=None,
                    adress=None,
                    ):

        if not first_name:
            raise TypeError("First name is required.")

        if not last_name:
            raise TypeError("Last name is required.")

        if not email:
            raise TypeError("email name is required.")

        if not password:
            raise TypeError("password name is required.")

        if not contact:
            raise TypeError("contact name is required.")

        if not adress:
            raise TypeError("address name is required.")

            user = self.model(first_name=first_name, last_name=last_name,
                            username=username, email=self.normalize_email(email), role='SU')
            user.set_password(password)
            user.is_active = True
            user.is_verified = True
            user.is_staff = True
            user.is_superuser = True
            user.save()

class User(AbstractUser):
    USER_ROLES = (
        ('HA', 'HOSPITAL ADMIN'),
        ('SU', 'SPONSOR USER'),
        ('HL', 'HEALTH TRACKER ADMIN')
    )
    role = models.CharField(max_length=3, choices=USER_ROLES, default='HA')
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    adress = models.CharField(max_length=60)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'contact', 'adress', 'username']

    objects = UserManager()

    def __str__(self):
        return self.email
