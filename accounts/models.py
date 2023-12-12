from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True)
    dob = models.DateField()
    is_completed = models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone','username','dob']





