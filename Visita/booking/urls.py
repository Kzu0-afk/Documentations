from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_home, name='booking_home'),
    path('list/', views.booking_list, name='booking_list'),
    path('create/', views.booking_create, name='booking_create'),
    path('delete/<int:pk>/', views.booking_delete, name='booking_delete'),
    path('rooms/<int:hotel_id>/', views.rooms_for_hotel, name='rooms_for_hotel'),  # Add this route
]
