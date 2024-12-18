# forms.py

from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['roomNumber', 'roomType', 'roomPrice', 'isAvailable','roomRating', 'roomDescription', 'hotel']
