from django import forms
from .models import Booking
from customer_entity.models import Customer

class BookingForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        empty_label="Select Customer",
        required=True
    )

    class Meta:
        model = Booking
        fields = ['customer', 'room', 'number_of_guests', 'check_in_date', 'check_out_date']
