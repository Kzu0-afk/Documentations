from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admin_home(request):
    return HttpResponse("Admin home page")

def admin_dashboard(request):
    # You can pass context if needed
    return render(request, 'admin_entity/admin_dashboard.html')