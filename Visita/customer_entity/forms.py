from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm

class CustomerSignupForm(UserCreationForm):
    contactNumber = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter contact number'}),
        help_text="Enter a valid contact number."
    )

    address = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter address'}),
    )

    class Meta:
        model = Customer
        fields = ['username', 'email', 'contactNumber', 'address', 'password1', 'password2']


class UpdateCustomerForm(forms.ModelForm):
    contactNumber = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter contact number'}),
        help_text="Enter a valid contact number."
    )

    class Meta:
        model = Customer
        fields = ['username', 'email', 'contactNumber', 'address']
