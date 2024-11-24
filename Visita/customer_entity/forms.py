from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Customer

class CustomerSignupForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'address', 'password1', 'password2']

class UpdateCustomerForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Leave blank to keep unchanged'}),
        help_text="Enter a new password if you'd like to change it."
    )

    class Meta:
        model = Customer
        fields = ['username', 'email', 'contactNumber', 'address', 'password']
