from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.PaymentListView.as_view(), name='payment_list'),  # List view
    path('new/', views.PaymentCreateView.as_view(), name='payment_create'),  # Create view
    path('<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='payment_update'),  # Update view
    path('<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment_delete'),  # Delete view
]
