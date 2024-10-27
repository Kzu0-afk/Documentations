from django.shortcuts import render
from django.http import  HttpResponse

def booking_home(request):
    return HttpResponse("Booking home page")
