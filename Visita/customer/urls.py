from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_home, name='customer_home'),
]