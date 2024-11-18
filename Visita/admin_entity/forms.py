from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdminEntity

class AdminSignupForm(UserCreationForm):
    class Meta:
        model = AdminEntity
        fields = ['username', 'password1', 'password2', 'email', 'departmentRole']

class UpdateAdminForm(forms.ModelForm):
    class Meta:
        model = AdminEntity
        fields = ['username', 'email', 'departmentRole']
