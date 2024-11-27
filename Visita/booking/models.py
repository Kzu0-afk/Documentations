from django.db import models
from customer_entity.models import Customer
from room.models import Room
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings', null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', null=True)
    booking_status = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(default=0)
    check_in_date = models.DateField(default=now().date(), null=False, blank=False)
    check_out_date = models.DateField(default=None, null=True, blank=False)

    def clean(self):
        if self.check_in_date < now().date():
            raise ValidationError("Check-in date cannot be in the past.")
        if self.check_out_date and self.check_out_date <= self.check_in_date:
            raise ValidationError("Check-out date must be after the check-in date.")

    def __str__(self):
        return f"Booking for {self.customer} in Room {self.room}"

