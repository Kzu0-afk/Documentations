# user_entity/backends.py
from customer_entity.models import Customer
from django.contrib.auth.backends import BaseBackend
from admin_entity.models import AdminEntity

class CustomerBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Customer.objects.get(username=username)
            if user.check_password(password):
                return user
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None

class AdminBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = AdminEntity.objects.get(username=username)
            if user.check_password(password):
                return user
        except AdminEntity.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return AdminEntity.objects.get(pk=user_id)
        except AdminEntity.DoesNotExist:
            return None