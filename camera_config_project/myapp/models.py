from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255)

class CustomUser(AbstractUser):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
