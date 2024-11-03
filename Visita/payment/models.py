from django.db import models

class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    paymentMethod = models.CharField(max_length=50)
    paymentAmount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentDate = models.DateField()
    paymentStatus = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.paymentID} - {self.paymentStatus}"
