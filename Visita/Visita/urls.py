"""
URL configuration for Visita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from hotel.views import landing_page

urlpatterns = [
    path('admin/', include('admin_entity.urls')),  # Make sure this matches exactly
    #admin_django for the main admin if you want to edit the database
    path('admin_django/', admin.site.urls),
    path('customer/', include('customer_entity.urls', namespace='customer_entity')),
    path('admin/', include('admin_entity.urls', namespace='admin_entity')),
    path('user/', include('user_entity.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('hotel/', include('hotel.urls')),
    path('booking/', include('booking.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('room/', include('room.urls')),
    path('', landing_page, name='home'),
]

