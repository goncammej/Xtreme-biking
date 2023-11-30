from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.SearchOrdersView.as_view(), name="search_orders"),
]