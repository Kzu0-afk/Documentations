from django.db import models
from admin_entity.models import AdminEntity 

class Hotel(models.Model):
    hotelID = models.AutoField(primary_key=True)
    hotelName = models.CharField(max_length=255)
    hotelDescription = models.TextField(null=True, blank=True)
    hotelRating = models.IntegerField(max_length=5, null=True, blank=True)
    admin = models.ForeignKey(AdminEntity, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.hotelName

