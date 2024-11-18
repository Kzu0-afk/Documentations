from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class CustomerSignupForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password1', 'password2', 'email', 'address']

class UpdateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'address']
