from django.db import models
from hotel.models import Hotel

class Room(models.Model):
    roomID = models.AutoField(primary_key=True)
    roomNumber = models.IntegerField()
    roomType = models.CharField(max_length=50)
    roomPrice = models.DecimalField(max_digits=10, decimal_places=2)
    isAvailable = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return f"Room {self.roomNumber} - {self.roomType}"
    
