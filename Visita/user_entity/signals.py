from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_backends

from django.apps import apps  # Dynamically import models
#signals.py
Customer = apps.get_model('customer_entity', 'Customer')
AdminEntity = apps.get_model('admin_entity', 'AdminEntity')

@receiver(post_save, sender=Customer)
def set_customer_backend(sender, instance, created, **kwargs):
    if created:
        backend = get_backends()[0]  # Assuming CustomerBackend is the first backend
        instance.backend = f"{backend.__module__}.{backend.__class__.__name__}"

@receiver(post_save, sender=AdminEntity)
def set_admin_backend(sender, instance, created, **kwargs):
    if created:
        backend = get_backends()[1]  # Assuming AdminBackend is the second backend
        instance.backend = f"{backend.__module__}.{backend.__class__.__name__}"
