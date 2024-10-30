from django.db import models

# Create your models here.

class Booking(models.Model):
    #foreignkey for customer
    #foreignkey for rooms
    
    bookingStatus = models.BooleanField(default=False)
    bookingStatus = models.CharField(max_length=255)
    numberOfGuests = models.IntegerField(default=0)
    
    checkInDate = models.DateTimeField(null=True, blank=True)
    checkOutDate = models.DateTimeField(null=True, blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        return f"Booking {self.id} for Room #roomId - #userID"