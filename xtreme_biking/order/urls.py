from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.SearchOrdersView, name="search_orders"),
]