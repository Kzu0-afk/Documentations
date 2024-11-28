from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from user_entity.utils import admin_required
from .models import Room
from .forms import RoomForm  # Make sure to create RoomForm in forms.py
from hotel.models import Hotel

def rooms_for_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, hotelID=hotel_id)  # Ensure `hotelID` is used
    rooms = Room.objects.filter(hotel=hotel, isAvailable=True)  # Fetch available rooms
    room_data = [
        {'id': room.roomID, 'roomNumber': room.roomNumber, 'roomType': room.roomType}
        for room in rooms
    ]
    return JsonResponse({'rooms': room_data})  # Return JSON response


class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.all()  # Fetch all rooms
        return render(request, 'room/room_list.html', {'rooms': rooms})

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_required, login_url='/admin_entity/login/'), name='dispatch')
class RoomCreateView(View):
    def get(self, request):
        form = RoomForm()
        return render(request, 'room/room_form.html', {'form': form})

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room:room_list')
        return render(request, 'room/room_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_required, login_url='/admin_entity/login/'), name='dispatch')
class RoomUpdateView(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        form = RoomForm(instance=room)
        return render(request, 'room/room_form.html', {'form': form})

    def post(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room:room_list')
        return render(request, 'room/room_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_required, login_url='/admin_entity/login/'), name='dispatch')
class RoomDeleteView(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        room.delete()
        return redirect('room:room_list')
