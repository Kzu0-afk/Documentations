# utils.py
def admin_required(user):
    return hasattr(user, 'adminentity')  # Ensure this matches the related name in your models

def customer_required(user):
    return hasattr(user, 'customer')  # Ensure this matches the related name in your models
