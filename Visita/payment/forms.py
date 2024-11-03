from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['paymentMethod', 'paymentAmount', 'paymentDate', 'paymentStatus']
