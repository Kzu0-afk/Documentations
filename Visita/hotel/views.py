from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hotel_home(request):
    return HttpResponse("Hotel home page")