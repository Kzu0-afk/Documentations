from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from hotel.models import Hotel
from room.models import Room
import logging
from .forms import BookingForm
from .models import Booking
from django.urls import reverse
from user_entity.utils import customer_required
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(customer_required, login_url='/customer_entity/login/')
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

logger = logging.getLogger(__name__)

@login_required
@user_passes_test(customer_required, login_url='/customer_entity/login/')
def booking_create(request):
    hotel_id = request.GET.get('hotel')
    room_id = request.GET.get('room')

    if hotel_id and room_id:
        room = get_object_or_404(Room, roomID=room_id, hotel__hotelID=hotel_id)
        hotel = room.hotel
        logger.info(f"Room fetched: {room}, Hotel: {hotel}")  # Log the room and hotel details
    else:
        logger.warning("Hotel ID or Room ID not provided. Redirecting to hotel list.")
        return redirect('hotel:hotel_list')  # Redirect if no hotel and room are specified

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.room = room
            booking.booking_status = 'Pending'
            booking.save()
            logger.info(f"Booking created with ID: {booking.id}, Room: {booking.room}")  # Log booking details
            return redirect(reverse('payment:payment_create', kwargs={'booking_id': booking.id}))
        else:
            logger.error(f"Booking form invalid: {form.errors}")  # Log form errors
    else:
        form = BookingForm(initial={'room': room})

    return render(request, 'booking/booking_form.html', {
        'form': form,
        'hotel': hotel,
        'room': room,
    })

@login_required
@user_passes_test(customer_required, login_url='/customer_entity/login/')
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        booking.delete()
        return redirect('booking:booking_list')
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})

@login_required
@user_passes_test(customer_required, login_url='/customer_entity/login/')
def booking_home(request):
    return render(request, 'booking/booking_home.html')

@login_required
@user_passes_test(customer_required, login_url='/customer_entity/login/')
def rooms_for_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel, isAvailable=True)  # Only available rooms
    room_data = [
        {'id': room.id, 'roomNumber': room.roomNumber, 'roomType': room.roomType}
        for room in rooms
    ]
    return JsonResponse({'rooms': room_data})
