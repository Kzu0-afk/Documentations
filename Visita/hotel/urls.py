from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_home, name='hotel_home'),
]
 