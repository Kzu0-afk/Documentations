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
        help_text="Leave blank if you don't want to change the password.",
    )

    class Meta:
        model = AdminEntity
        fields = ['username', 'email', 'contactNumber', 'departmentRole', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill the password field with the existing hashed password (not visible to the user).
        if self.instance and self.instance.pk:
            self.fields['password'].initial = self.instance.password

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.cleaned_data['password']:
            # If the password field is left blank, retain the existing password.
            user.password = self.instance.password
        elif commit:
            user.set_password(self.cleaned_data['password'])  # Hash the new password.
        if commit:
            user.save()
        return user
