from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.backends import BaseBackend    

# Create your models here
# 
#  Inheriting from User model class and extending it .

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=256)
    username = m

    
    
