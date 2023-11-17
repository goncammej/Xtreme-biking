from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('orders/', views.orders, name='orders'),
    path('logout/', views.logout, name='logout'),
    path('orders_details/', views.order_details, name='orders_details'),
    path('incident/', views.incident, name='incident'),
]