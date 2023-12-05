import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest, JsonResponse

from store.models import Product
from client.models import CustomerPaymentMethod, CustomerShipping, Customer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from store.utils import cartData

import stripe

stripe.api_key = 'sk_test_51OHZkjLj1aqlpDCrIBuI2Sefe88XpHAO4FhK6iqXcu9JJj1qVFl0P1wkVBFj6KomvyygGKv7agAqhrhufG3okYfU00IpZYyFCx'


def cart(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
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
