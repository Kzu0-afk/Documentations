from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .models import Hotel
from .forms import HotelForm
from user_entity.utils import admin_required  # Import admin_required

# Landing page view (accessible by all)
def landing_page(request):
    return render(request, 'hotel/landing_page.html')

# Hotel list (accessible by all)
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
            form.save()
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
            form.save()
            return redirect('hotel:hotel_list')
        return render(request, 'hotel/hotel_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(admin_required, login_url='/admin_entity/login/'), name='dispatch')
class HotelDeleteView(View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        hotel.delete()
        return redirect('hotel:hotel_list')
