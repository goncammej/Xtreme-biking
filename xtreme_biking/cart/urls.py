from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('create_payment', views.create_payment, name='create_payment'),
]