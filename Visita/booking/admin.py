from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'room', 'booking_status', 'check_in_date', 'check_out_date')
    list_filter = ('booking_status', 'check_in_date', 'check_out_date')
    search_fields = ('customer__username', 'room__roomType', 'room__hotel__hotelName')
