from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomListView.as_view(), name='room_list'),
    path('new/', views.RoomCreateView.as_view(), name='room_create'),
    path('<int:pk>/edit/', views.RoomUpdateView.as_view(), name='room_update'),
    path('<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room_delete'),
]