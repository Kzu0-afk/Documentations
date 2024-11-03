from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Room
from .forms import RoomForm  # Make sure to create RoomForm in forms.py

class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'room/room_list.html', {'rooms': rooms})

class RoomCreateView(View):
    def get(self, request):
        form = RoomForm()
        return render(request, 'room/room_form.html', {'form': form})

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
        return render(request, 'room/room_form.html', {'form': form})

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
            return redirect('room_list')
        return render(request, 'room/room_form.html', {'form': form})

class RoomDeleteView(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        room.delete()
        return redirect('room_list')
