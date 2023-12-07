import datetime
import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.template.loader import render_to_string

from store.models import Product
from client.models import CustomerPaymentMethod, CustomerShipping, Customer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from store.utils import cartData, guestOrder

from django.test import Client

import stripe

from order.models import Order, ShippingAddress

stripe.api_key = 'sk_test_51OHZkjLj1aqlpDCrIBuI2Sefe88XpHAO4FhK6iqXcu9JJj1qVFl0P1wkVBFj6KomvyygGKv7agAqhrhufG3okYfU00IpZYyFCx'


def cart(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    print(context)
    return render(request, 'cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    domain = settings.BASE_URL
    path = ""
    successUrl = f'http://{domain}/{path}'

    context = {'order': order, 'successUrl': successUrl,
               'cartItems': cartItems}

    if request.user.is_authenticated:
        context['preferred_method'] = CustomerPaymentMethod.objects.get(
            customer=request.user.customer)
        context['addresses'] = CustomerShipping.objects.filter(
            customer=request.user.customer)
        context['addresses_count'] = len(context['addresses'])
        context['name'] = request.user.name
        context['email'] = request.user.email

    if (cartItems > 0):
        return render(request, 'checkout.html', context)
    else:
        return redirect("frontpage")


@csrf_exempt
def create_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            total = int(float(data['total']) * 100)
            print(total)
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=total,
                currency='eur',
                # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse(error=str(e)), 403


def success(request):
    data_param = request.GET.get('data')

    if data_param:
        try:
            # Parse the JSON data
            transaction_id = datetime.datetime.now().timestamp()
            data = json.loads(data_param)

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

        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            return HttpResponse(f"Error decoding JSON data: {str(e)}", status=400)
    else:
        # Handle missing or invalid data parameter
        return HttpResponse("Invalid data parameter", status=400)
