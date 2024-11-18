from django.urls import path  # Make sure this import is included
from . import views
app_name = 'admin_entity'

urlpatterns = [
    path('signup/', views.admin_signup_view, name='signup'),
    path('login/', views.admin_login_view, name='login'),
    path('profile/', views.admin_profile_view, name='profile'),
    # path('update_profile/', views.admin_update_profile_view, name='update_profile'),
    path('delete_account/', views.admin_delete_account_view, name='delete_account'),
]
