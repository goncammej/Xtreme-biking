from django.urls import path
from store import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('product_details/<int:producto_id>/',
         views.product_details, name='product_details'),
    path("search/", views.SearchResultsView, name="search_results"),
]
