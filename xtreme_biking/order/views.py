from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from store.utils import cartData

from .models import Order
from django.db.models import Q


def SearchOrdersView(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {"request": request, "order": None, "cartItems": cartItems}
    reference = request.GET.get("r")
    if reference:
        try:
            context['order'] = Order.objects.get(
                transaction_id=reference, complete=True)
        except:
            context['order'] = None

    return render(request, 'search_orders.html', context)
