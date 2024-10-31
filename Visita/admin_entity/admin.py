from django.contrib import admin
from .models import AdminEntity
# Register your models here.

@admin.register(AdminEntity)
class AdminEntityAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'contactNumber', 'registerDate', 'departmentRole')