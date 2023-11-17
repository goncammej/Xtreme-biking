from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest

# Create your views here.

def cart_view(request):
    cart_items = [
        {'product': {'name': 'Producto 1', 'price': 10}, 'quantity': 2, 'total': 20},
        {'product': {'name': 'Producto 2', 'price': 20}, 'quantity': 1, 'total': 20},
        {'product': {'name': 'Producto 3', 'price': 30}, 'quantity': 3, 'total': 90},
    ]
    cart_total = 130
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)