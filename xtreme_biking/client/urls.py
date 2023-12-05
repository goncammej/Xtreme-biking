from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.client_dashboard, name='client_dashboard'),
    path('addresses', views.client_addresses, name='client_addresses'),
    path('addresses/create', views.create_address, name='create_address'),
    path('addresses/edit/<int:address_id>/',
         views.edit_address, name='edit_address'),
    path('addresses/remove/<int:address_id>/',
         views.remove_address, name='remove_address'),
    path('addresses/predetermined/<int:address_id>/',
         views.predetermined_address, name='predetermined_address'),
    path('orders', views.client_orders, name='client_orders'),
]
