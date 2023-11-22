from django.urls import path
from store import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_details/<int:producto_id>/', views.product_details, name='product_details'),
    path('product_details/<int:producto_id>/rating_new/', views.create_rating, name='create_rating'),
    path('buscar-productos/', views.buscar_productos, name='buscar_productos'),
]