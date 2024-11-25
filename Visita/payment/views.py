from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Payment
from .forms import PaymentForm  # Make sure to create PaymentForm in forms.py

class PaymentListView(View):
    def get(self, request):
        payments = Payment.objects.all()
        return render(request, 'payment/payment_list.html', {'payments': payments})

class PaymentCreateView(View):
    def get(self, request):
        form = PaymentForm()
        return render(request, 'payment/payment_form.html', {'form': form})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment:payment_list')  # Ensure this redirect is correct
        return render(request, 'payment/payment_form.html', {'form': form})
    
class PaymentUpdateView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(instance=payment)
        return render(request, 'payment/payment_form.html', {'form': form})

    def post(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment:payment_list')
        return render(request, 'payment/payment_form.html', {'form': form})

class PaymentDeleteView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()
        return redirect('payment:payment_list')
