from django.urls import path
from . import views

app_name = 'customer_entity'

urlpatterns = [
    path('signup/', views.customer_signup_view, name='signup'),
    path('login/', views.customer_login_view, name='login'),
    path('profile/', views.customer_profile_view, name='profile'),
    path('edit_profile/', views.update_customer_profile_view, name='edit_profile'),
    path('delete_account/', views.customer_delete_account_view, name='delete_account'),
    path('logout/', views.customer_logout_view, name='logout'),  # Add this line
    path('landing_page/', views.customer_landing_page, name='landing_page'),
]
