from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    name = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255, unique=True)
    password= models.CharField(max_length= 255)
    

    USERNAME_FIELD: 'email'
    REQUIRED_FIELDS: []
