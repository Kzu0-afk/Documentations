from django.contrib import admin
from .models import Customer
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','first_name', 'last_name', 'contactNumber', 'registerDate', 'address')
