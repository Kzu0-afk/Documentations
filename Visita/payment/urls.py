from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.PaymentListView.as_view(), name='payment_list'),
    path('create/<int:booking_id>/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('update/<int:pk>/', views.PaymentUpdateView.as_view(), name='payment_update'),
    path('delete/<int:pk>/', views.PaymentDeleteView.as_view(), name='payment_delete'),
]

