from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Order
from django.db.models import Q

class SearchOrdersView(ListView):
    model = Order
    template_name = "search_orders.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Order.objects.filter(
            Q(transaction_id=query)
        )
        return object_list
