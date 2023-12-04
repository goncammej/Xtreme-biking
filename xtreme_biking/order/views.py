from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Order
from django.db.models import Q
    
def SearchOrdersView(request):
    context = {"request": request, "order": None}
    reference = request.GET.get("r")
    context['order'] = Order.objects.get(transaction_id = reference)
    
    return render(request, 'search_orders.html', context)