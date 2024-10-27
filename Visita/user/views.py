from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def user_home(request):
    return HttpResponse("User home page")