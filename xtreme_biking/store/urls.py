from django.urls import path
from . import views

urlpatterns = [
        path('about/', views.about, name='about'),
        path('product_list/', views.product_list, name='product_list'),
        path('product_details/', views.product_details, name='product_details'),
]