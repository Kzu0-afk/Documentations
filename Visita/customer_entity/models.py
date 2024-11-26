from django.db import models
from user_entity.models import User
from django.db import models

# Create your models here.

class Customer(User):
    #add rani nako para nay difference and customer ug admin ug para ma link sa user na superclass
    #kamo na bahala sa views ana
    address = models.CharField(max_length=255)

class Hotel(models.Model):
    hotelName = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.username}"
    