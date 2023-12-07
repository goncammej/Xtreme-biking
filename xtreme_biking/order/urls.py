from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.SearchOrdersView, name="search_orders"),
    path('review/<int:order_id>/', views.create_review, name='create_review'),
    path('review/edit/<int:order_id>/', views.edit_review, name='edit_review'),
    path('claim/<int:order_id>/', views.create_claim, name='create_claim'),
    path('claim/edit/<int:order_id>/', views.edit_claim, name='edit_claim'),
]