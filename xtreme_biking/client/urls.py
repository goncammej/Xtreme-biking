from django.urls import path
from . import views

urlpatterns = [
     path('dashboard', views.client_dashboard, name='client_dashboard'),
     path('addresses', views.client_addresses, name='client_addresses'),
     path('orders', views.client_orders, name='client_orders'),
]