from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_home, name='room_home'),
]
