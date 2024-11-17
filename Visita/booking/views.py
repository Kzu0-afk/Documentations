from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from room.models import Room


def booking_create(request):
    # Handle POST Request
    if request.method == "POST":
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user.customer  # Set the logged-in customer
            booking.booking_status = "Pending"  # Default status for new bookings
            booking.save()

            # Update room availability
            booking.room.isAvailable = False
            booking.room.save()

            return redirect('booking_home')  # Redirect to booking home or list

    # Handle GET Request
    else:
        form = BookingForm(user=request.user)
    return render(request, 'booking/booking_form.html', {'form': form})


@login_required  # Ensure the user is logged in
def booking_home(request):
    try:
        # Fetch bookings only for the logged-in customer
        bookings = Booking.objects.filter(customer=request.user.customer)
    except AttributeError:
        # Redirect to login if the user is not associated with a customer
        return redirect('login')

    return render(request, 'booking/booking_list.html', {'bookings': bookings})