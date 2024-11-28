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
        # Calculate payment amount based on room price and duration
        stay_duration = (booking.check_out_date - booking.check_in_date).days
        payment_amount = booking.room.roomPrice * stay_duration

        form = PaymentForm(initial={'booking': booking})
        return render(request, 'payment/payment_form.html', {
            'form': form, 
            'booking': booking,
            'payment_amount': payment_amount
        })

    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.paymentAmount = float(request.POST.get('paymentAmount'))
            payment.paymentMethod = request.POST.get('paymentMethod')
            
            # Handle card details if payment method is credit or debit card
            if payment.paymentMethod in ['credit_card', 'debit_card']:
                payment.cardNumber = request.POST.get('cardNumber')
                payment.cardHolder = request.POST.get('cardHolder')
                payment.expiryDate = request.POST.get('expiryDate')
                payment.cvv = request.POST.get('cvv')
            
            payment.save()
            booking.booking_status = 'Paid'
            booking.save()
            return redirect('payment:payment_list')
        
        # If form is not valid, recalculate payment_amount
        stay_duration = (booking.check_out_date - booking.check_in_date).days
        payment_amount = booking.room.roomPrice * stay_duration
        return render(request, 'payment/payment_form.html', {
            'form': form, 
            'booking': booking,
            'payment_amount': payment_amount
        })

class PaymentUpdateView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(instance=payment)
        return render(request, 'payment/payment_form.html', {
            'form': form, 
            'booking': payment.booking,
            'payment_amount': payment.paymentAmount
        })

    def post(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.paymentMethod = request.POST.get('paymentMethod')
            
            # Handle card details if payment method is credit or debit card
            if payment.paymentMethod in ['credit_card', 'debit_card']:
                payment.cardNumber = request.POST.get('cardNumber')
                payment.cardHolder = request.POST.get('cardHolder')
                payment.expiryDate = request.POST.get('expiryDate')
                payment.cvv = request.POST.get('cvv')
            
            payment.save()
            return redirect('payment:payment_list')
        return render(request, 'payment/payment_form.html', {
            'form': form, 
            'booking': payment.booking,
            'payment_amount': payment.paymentAmount
        })

class PaymentDeleteView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()
        return redirect('payment:payment_list')