from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'room', 'bookingStatus', 'numberOfGuests', 'checkInDate', 'checkOutDate']
        widgets = {
            'checkInDate': forms.DateInput(attrs={'type': 'date'}),
            'checkOutDate': forms.DateInput(attrs={'type': 'date'}),
        }
