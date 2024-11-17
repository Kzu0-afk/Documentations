from django.shortcuts import render
from .forms import BookingForm
from .models import Booking

def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # Display the submitted data after saving the booking
            return render(request, 'booking/booking_success.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})
