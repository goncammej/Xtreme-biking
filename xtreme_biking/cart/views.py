from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest

from store.models import Product
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from store.utils import cartData

# Create your views here.


def cart(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)

def checkout(request):
    return render(request, 'checkout.html')
