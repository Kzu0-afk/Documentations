from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdminEntity

class AdminSignupForm(UserCreationForm):
    contactNumber = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter contact number'}),
        help_text="Enter a valid contact number."
    )

    departmentRole = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter department role'}),
        help_text="Enter the role in the department."
    )

    class Meta:
        model = AdminEntity
        #i think the error is password1 and password 2
        fields = ['username', 'email', 'contactNumber', 'departmentRole', 'password1', 'password2']


class UpdateAdminForm(forms.ModelForm):
    contactNumber = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter contact number'}),
        help_text="Enter a valid contact number."
    )

    class Meta:
        model = AdminEntity
        fields = ['username', 'email', 'contactNumber', 'departmentRole']
