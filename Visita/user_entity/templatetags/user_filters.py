from django import template

register = template.Library()

@register.filter
def customer_required(user):
    return hasattr(user, 'customer')  # Check if the user is a Customer

@register.filter
def admin_required(user):
    return hasattr(user, 'adminentity')  # Check if the user is an AdminEntity