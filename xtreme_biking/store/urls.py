from django.urls import path
from store import views

urlpatterns = [
    path('product_details/<int:producto_id>/', views.product_details, name='product_details'),
    path('bike_catalogue/', views.bike_catalogue, name='bike_catalogue'),
    path('accessories_catalogue/', views.accessories_catalogue, name='accessories_catalogue'),
    path('product_details/<int:producto_id>/ratings/', views.get, name='get'),
    path('product_details/<int:producto_id>/ratings/new/', views.post, name='post'),
]