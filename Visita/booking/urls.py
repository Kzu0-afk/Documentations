from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_home, name='booking_home'),
    path('list/', views.booking_list, name='booking_list'),
    path('create/', views.booking_create, name='booking_create'),
    path('delete/<int:pk>/', views.booking_delete, name='booking_delete'),
]
