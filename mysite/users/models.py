from pyexpat import model
from re import M
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

  
class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True) 
    role = models.CharField(max_length=16)
    age = models.CharField(max_length=16)
    bio = models.CharField(max_length=200)
      

  