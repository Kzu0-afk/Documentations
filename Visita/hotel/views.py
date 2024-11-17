from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Hotel
from .forms import HotelForm  # Ensure this form is created in forms.py

# Landing page view
def landing_page(request):
    return render(request, 'hotel/landing_page.html')

# Functional view for hotel list
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/hotel_list.html', {'hotels': hotels})

# Simple hotel home placeholder view
def hotel_home(request):
    return HttpResponse("Hotel home page")

# Class-based views (CBVs) for Hotel operations
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
            return redirect('hotel_list')  # Redirect to the hotel list after saving
        return render(request, 'hotel/hotel_form.html', {'form': form})  # Return form with errors

class HotelUpdateView(View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)  # Fetch the hotel object
        form = HotelForm(instance=hotel)  # Pre-fill the form with existing hotel data
        return render(request, 'hotel/hotel_form.html', {'form': form})

    def post(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')  # Redirect after successful update
        return render(request, 'hotel/hotel_form.html', {'form': form})

class HotelDeleteView(View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)  # Fetch the hotel object
        hotel.delete()  # Delete the object
        return redirect('hotel_list')  # Redirect to the list view
