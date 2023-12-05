import datetime
import json
from store.utils import cartData, guestOrder
from store.models import Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.views.generic.base import View
from django.http import JsonResponse
from django import forms
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail

import random

from order.models import Order, OrderItem, ShippingAddress
from client.models import Customer, CustomerShipping, CustomerPaymentMethod

from django.db.models import Q


def about(request):
    return render(request, 'about.html')


def frontpage(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()[:3]
    context = {"products": products, "cartItems": cartItems}

    return render(request, 'home.html', context)


def catalogue(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products_all = sorted(Product.objects.all()[
                          :3], key=lambda x: random.random())
    products_mountain = sorted(Product.objects.filter(
        category="Bicleta de montaña")[:3], key=lambda x: random.random())
    products_urban = sorted(Product.objects.filter(category="Bicicleta urbana")[
                            :3], key=lambda x: random.random())
    products_road = sorted(Product.objects.filter(
        category="Bicicleta de carretera")[:3], key=lambda x: random.random())
    products_sustitution = sorted(Product.objects.filter(
        category="Pieza de sustitución")[:3], key=lambda x: random.random())

    context = {"products_all": products_all, "products_mountain": products_mountain, "products_urban": products_urban,
               "products_road": products_road, "products_sustitution": products_sustitution, "cartItems": cartItems}

    return render(request, 'product_list.html', context)


def product_details(request, producto_id):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    product = get_object_or_404(Product, pk=producto_id)

    context = {'product': product, "cartItems": cartItems}
    return render(request, 'product_details.html', context)


def SearchResultsView(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {"request": request, "products": None, "cartItems": cartItems}
    query = request.GET.get("q")
    category = request.GET.get("c")
    if category and query:

        if category == "todos":
            context['products'] = Product.objects.filter(
                Q(title__icontains=query)
            )
        else:
            context['products'] = Product.objects.filter(
                Q(title__icontains=query) & Q(title__icontains=category)
            )
    elif category and not query:

        if category == "todos":
            context['products'] = Product.objects.all()
        else:
            context['products'] = Product.objects.filter(
                Q(category__icontains=category)
            )
    elif query and not category:
        context['products'] = Product.objects.filter(
            Q(category__icontains=query) | Q(title__icontains=query)
        )
    return render(request, 'search_results.html', context)


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
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'delete':
        orderItem.quantity = 0
    elif action == 'add-quantity':
        orderItem.quantity = (orderItem.quantity + quantity)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)["data"]

    print(data)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        if data['selected_address'] == 'null':
            CustomerShipping.objects.create(
                customer=customer,
                address=data['address'],
                city=data['city'],
                state=data['locality'],
                zipcode=data['zipcode'],
                predetermined=True
            )
    else:
        customer, order = guestOrder(request, data)

    total = order.get_cart_total

    if data['shipping_method'] == 'UPS_S':
        total += 10.00
    elif data['shipping_method'] == 'US_S':
        total += 30.00

    order.transaction_id = transaction_id
    order.total = total

    order.complete = True
    order.save()

    if data['selected_address'] != 'null':
        selected_address = CustomerShipping.objects.get(
            id=int(data['selected_address']))
        print(selected_address)
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=selected_address.address,
            city=selected_address.city,
            state=selected_address.state,
            zipcode=selected_address.zipcode,
        )
    else:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['address'],
            city=data['city'],
            state=data['locality'],
            zipcode=data['zipcode'],
        )

    """ send_mail(
    "Gracias por comprar en Xtreme Biking",
    f"El identificador de tu pedido es {order.transaction_id}. Puedes consultar el estado de tu pedido a través del siguiente enlace ",
    "from@example.com",
    ["to@example.com"],
    fail_silently=False,
    ) """

    return JsonResponse('Payment submitted..', safe=False)


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)
