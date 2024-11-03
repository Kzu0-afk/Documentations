from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def customer_home(request):
    return HttpResponse("Customer home page")
