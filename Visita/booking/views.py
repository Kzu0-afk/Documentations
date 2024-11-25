from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking:booking_list')
    else:
        form = BookingForm()
        return redirect('booking:booking_form')
    return render(request, 'booking/booking_form.html', {'form': form})

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        booking.delete()
        return redirect('booking:booking_list')
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})

def booking_home(request):
    return render(request, 'booking/booking_home.html')