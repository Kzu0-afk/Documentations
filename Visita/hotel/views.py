from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Hotel
from .forms import HotelForm  # Create a form for Hotel in forms.py
from django.shortcuts import render

def hotel_home(request):
    return HttpResponse("Hotel home page")

class HotelListView(View):
    def get(self, request):
        hotels = Hotel.objects.all()
        return render(request, 'hotel/hotel_list.html', {'hotels': hotels})

class HotelCreateView(View):
    def get(self, request):
        form = HotelForm()
        return render(request, 'hotel/hotel_form.html', {'form': form})

    def post(self, request):
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
        return render(request, 'hotel/hotel_form.html', {'form': form})

class HotelUpdateView(View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = HotelForm(instance=hotel)
        return render(request, 'hotel/hotel_form.html', {'form': form})

    def post(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
        return render(request, 'hotel/hotel_form.html', {'form': form})

class HotelDeleteView(View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        hotel.delete()
        return redirect('hotel_list')
