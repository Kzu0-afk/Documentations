from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    contactNumber = models.CharField(max_length=15, blank=True, null=True)
    registerDate = models.DateTimeField(default=now)
    pass
    
    def __str__(self):
        return self.username
    

    
