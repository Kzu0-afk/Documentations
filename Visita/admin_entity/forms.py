from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import AdminEntity

class AdminSignupForm(UserCreationForm):
    class Meta:
        model = AdminEntity
        fields = ['username', 'email', 'departmentRole', 'password1', 'password2']

class UpdateAdminForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Leave blank to keep unchanged'}),
        help_text="Enter a new password if you'd like to change it."
    )

    class Meta:
        model = AdminEntity
        fields = ['username', 'email', 'contactNumber', 'departmentRole', 'password']
