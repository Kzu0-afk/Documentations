from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View

from room.models import Room
from .models import Hotel
from .forms import HotelForm
from user_entity.utils import admin_required  # Import admin_required

# Landing page view (accessible by all)
def landing_page(request):
    return render(request, 'hotel/landing_page.html')

# New function to render the hotel homepage
def hotel_homepage(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/hotel_homepage.html', {'hotels': hotels})

# Functional view for hotel list
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/hotel_list.html', {'hotels': hotels})

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_required, login_url='/admin_entity/login/'), name='dispatch')
class HotelCreateView(View):
    def get(self, request):
        form = HotelForm()
        return render(request, 'hotel/hotel_form.html', {'form': form})

    def post(self, request):
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = form.save(commit=False)  # Don't save to the database yet
            hotel.admin = request.user  # Assign the currently logged-in admin entity
            hotel.save()  # Save to the database
            return redirect('hotel:hotel_list')
        return render(request, 'hotel/hotel_form.html', {'form': form})



@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_required, login_url='/admin_entity/login/'), name='dispatch')
class HotelUpdateView(View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = HotelForm(instance=hotel)
        return render(request, 'hotel/hotel_form.html', {'form': form})

    def post(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()  # No need to modify the `admin` field here
            return redirect('hotel:hotel_list')
        return render(request, 'hotel/hotel_form.html', {'form': form})



@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_required, login_url='/admin_entity/login/'), name='dispatch')
class HotelDeleteView(View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        hotel.delete()
        return redirect('hotel:hotel_list')

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = Room.objects.filter(hotel=hotel)
    return render(request, 'hotel/hotel_detail.html', {
        'hotel': hotel,
        'rooms': rooms
    })