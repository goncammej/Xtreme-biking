from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.admin_orders_details, name='admin_orders'),
]