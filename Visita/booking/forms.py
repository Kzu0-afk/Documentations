from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'number_of_guests', 'check_in_date', 'check_out_date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Dynamically filter room options based on availability
        self.fields['room'].queryset = self.fields['room'].queryset.filter(isAvailable=True)
