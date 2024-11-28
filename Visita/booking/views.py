from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from hotel.models import Hotel
from room.models import Room
from .forms import BookingForm
from .models import Booking
from django.urls import reverse
from user_entity.utils import customer_required
from django.contrib.auth.decorators import login_required, user_passes_test

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})




@login_required
@user_passes_test(customer_required, login_url='/customer_entity/login/')
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user  # Automatically assign the logged-in customer
            booking.save()
            return redirect(reverse('payment:payment_create', kwargs={'booking_id': booking.id}))
    else:
        form = BookingForm()

    # Pass all hotels to the template for the dropdown
    hotels = Hotel.objects.all()

    return render(request, 'booking/booking_form.html', {'form': form, 'hotels': hotels})


def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        booking.delete()
        return redirect('booking:booking_list')
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})

def booking_home(request):
    return render(request, 'booking/booking_home.html')

def rooms_for_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel, isAvailable=True)  # Only available rooms
    room_data = [
        {'id': room.id, 'roomNumber': room.roomNumber, 'roomType': room.roomType}
        for room in rooms
    ]
    return JsonResponse({'rooms': room_data})
