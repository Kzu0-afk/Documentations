from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def payment_home(request):
    return HttpResponse("Payment home page")