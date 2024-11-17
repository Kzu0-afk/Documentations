from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_home, name='booking_home'),
    path('create/', views.booking_create, name='booking_create'),
]
