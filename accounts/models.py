from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True)
    dob = models.DateField()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone','username','dob']

class Preferences(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    preference = models.CharField(max_length=50)

    