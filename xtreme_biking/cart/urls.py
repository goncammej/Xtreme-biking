from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('delete/<int:product_id>/', views.delete_product_from_cart, name='delete_product_from_cart'),
]