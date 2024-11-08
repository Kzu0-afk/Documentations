from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_home, name='landing_page'),
    path('list/', views.HotelListView.as_view(), name='hotel_list'),
    path('new/', views.HotelCreateView.as_view(), name='hotel_create'),
    path('<int:pk>/edit/', views.HotelUpdateView.as_view(), name='hotel_update'),
    path('<int:pk>/delete/', views.HotelDeleteView.as_view(), name='hotel_delete'),
]
