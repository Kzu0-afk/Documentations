from django.db import models
from admin_entity.models import AdminEntity 

class Hotel(models.Model):
    hotelID = models.AutoField(primary_key=True)
    hotelName = models.CharField(max_length=255)
    admin = models.ForeignKey(AdminEntity, on_delete=models.CASCADE) #null=True #temporarily fill the admin rows as null b4 having the main admin
    def __str__(self):
        return self.hotelName

