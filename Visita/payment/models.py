from django.db import models
from booking.models import Booking

class Payment(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define id field
    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name='payment',
        null=True,
        blank=True
    )
    paymentMethod = models.CharField(max_length=50)
    paymentAmount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentDate = models.DateField(auto_now_add=True)
    paymentStatus = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Payment for Booking {self.booking.id if self.booking else 'N/A'} - {self.paymentStatus}"