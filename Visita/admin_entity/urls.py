from django.urls import path
from . import views

app_name = 'admin_entity'

urlpatterns = [
    path('signup/', views.admin_signup_view, name='signup'),
    path('login/', views.admin_login_view, name='login'),
    path('profile/', views.admin_profile_view, name='profile'),
    path('update_profile/', views.update_admin_profile_view, name='update_profile'),
    path('delete_account/', views.admin_delete_account_view, name='delete_account'),
    path('logout/', views.admin_logout_view, name='logout'),  # Add this line
]

