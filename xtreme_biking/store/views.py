import json
from store.utils import cartData
from store.models import Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.views.generic.base import View
from django.http import JsonResponse
from django import forms
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from order.models import Order, OrderItem

from django.db.models import Q

def about(request):
    return render(request, 'about.html')

def product_list(request):
    return render(request, 'product_list.html')

def frontpage(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products= Product.objects.all()[:3]
    context = {"products": products, "cartItems": cartItems}
    
    return render(request, 'home.html', context)

def catalogue(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}

    return render(request, 'product_list.html', context)

def product_details(request, producto_id):
    product = get_object_or_404(Product, pk=producto_id)
    
    context = {'product': product}
    return render(request, 'product_details.html', context)

class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'
    
    def get_queryset(self):
        query = str(self.request.GET.get("q"))
        category = str(self.request.GET.get("c"))
        if category and query:
            return Product.objects.filter(
                Q(title__icontains=query) & Q(category__icontains=category)
            )
        elif category and not query:
            return Product.objects.filter(
                Q(category__icontains=category)
            )
        elif query and not category:
            return Product.objects.filter(
                Q(category__icontains=query | Q(category__icontains=query))
            )
    
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    quantity = data['quantity']
    print('Action:', action)
    print('Product:', productId)
    print('Quantity:', quantity)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'delete':
        orderItem.delete()
    elif action == 'add-quantity':
        orderItem.quantity = (orderItem.quantity + quantity)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)