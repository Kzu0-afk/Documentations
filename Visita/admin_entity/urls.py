from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
       path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),  # Ensure this matches
]