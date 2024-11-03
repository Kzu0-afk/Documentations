from django.db import models

class Hotel(models.Model):
    hotelID = models.AutoField(primary_key=True)
    hotelName = models.CharField(max_length=255)

    def __str__(self):
        return self.hotelName
