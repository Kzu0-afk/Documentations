from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def room_home(reqeust):
    return HttpResponse("Room home page")