from django.urls import path  # Make sure this import is included
from . import views
app_name = 'customer_entity'

urlpatterns = [
    path('signup/', views.customer_signup_view, name='signup'),
    path('login/', views.customer_login_view, name='login'),
    path('profile/', views.customer_profile_view, name='profile'),
    # path('update_profile/', views.customer_update_profile_view, name='update_profile'),
    path('delete_account/', views.customer_delete_account_view, name='delete_account'),
]
