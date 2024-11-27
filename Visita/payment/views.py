from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Payment
from .forms import PaymentForm
from booking.models import Booking

class PaymentListView(View):
    def get(self, request):
        payments = Payment.objects.all()
        return render(request, 'payment/payment_list.html', {'payments': payments})

class PaymentCreateView(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        initial_data = {
            'paymentAmount': booking.room.price * (booking.check_out_date - booking.check_in_date).days,
            'booking': booking,
        }
        form = PaymentForm(initial=initial_data)
        return render(request, 'payment/payment_form.html', {'form': form, 'booking': booking})

    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()
            booking.booking_status = 'Paid'
            booking.save()
            return redirect('payment:payment_list')
        return render(request, 'payment/payment_form.html', {'form': form, 'booking': booking})

class PaymentUpdateView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(instance=payment)
        return render(request, 'payment/payment_form.html', {'form': form, 'booking': payment.booking})

    def post(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment:payment_list')
        return render(request, 'payment/payment_form.html', {'form': form, 'booking': payment.booking})

class PaymentDeleteView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()
        return redirect('payment:payment_list')

