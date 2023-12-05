from django.shortcuts import render, get_object_or_404

from order.models import Order
from store.utils import cartData
from . import forms
from .models import CustomerPaymentMethod, CustomerShipping
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect


@login_required
def client_dashboard(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user
    orders = Order.objects.filter(customer=user.customer)
    payment_method = CustomerPaymentMethod.objects.get(customer=user.customer)

    payment_form = forms.PaymentMethodForm(
        initial={'customer': user.customer, "method": payment_method.method})
    if request.method == 'POST':
        if 'payment_info' in request.POST:
            payment_form = forms.PaymentMethodForm(
                request.POST, instance=payment_method)
            if payment_form.is_valid():
                payment_form.save()

    context = {"user": user, "orders": orders,
               "payment_method": payment_method, 'payment_form': payment_form, 'cartItems': cartItems}
    return render(request, 'client_dashboard.html', context)


@login_required
def client_addresses(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user

    try:
        predetermined_address = CustomerShipping.objects.get(
            customer=user.customer, predetermined=True)
        addresses = CustomerShipping.objects.filter(
            customer=user.customer).exclude(id=predetermined_address.id)
    except:
        addresses = None
        predetermined_address = None
    context = {"addresses": addresses,
               'predetermined': predetermined_address, 'cartItems': cartItems}
    return render(request, 'client_addresses.html', context)


@login_required
def create_address(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user
    shipping_form = forms.ShippingAdressForm(user=user)
    if request.method == 'POST':
        if 'shipping_info' in request.POST:
            shipping_form = forms.ShippingAdressForm(
                request.POST, user=user)
            if shipping_form.is_valid():
                shipping_instance = shipping_form.save(commit=False)
                shipping_instance.customer = user.customer
                shipping_instance.save()
                return redirect('client_addresses')
    if request.method == 'GET':
        context = {"user": user, 'form': shipping_form, 'cartItems': cartItems}
        return render(request, 'client_addresses_form.html', context)


@login_required
def edit_address(request, address_id):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user
    shipping_address = get_object_or_404(
        CustomerShipping, customer=user.customer, id=address_id)
    shipping_form = forms.ShippingAdressForm(
        initial={'customer': user.customer, 'address': shipping_address.address, "city": shipping_address.city, "state": shipping_address.state, "zipcode": shipping_address.zipcode})
    if request.method == 'POST':
        if 'shipping_info' in request.POST:
            shipping_form = forms.ShippingAdressForm(
                request.POST, instance=shipping_address)
            if shipping_form.is_valid():
                shipping_form.save()
                return redirect('client_addresses')
    if request.method == 'GET':
        context = {"user": user, "shipping_address": shipping_address,
                   'form': shipping_form, 'cartItems': cartItems}
        return render(request, 'client_addresses_form.html', context)


@login_required
def predetermined_address(request, address_id):
    user = request.user
    shipping_address = get_object_or_404(
        CustomerShipping, customer=user.customer, id=address_id)
    previous_address = CustomerShipping.objects.get(
        customer=user.customer, predetermined=True)
    previous_address.predetermined = False
    previous_address.save()

    shipping_address.predetermined = True
    shipping_address.save()

    return redirect("client_addresses")


@login_required
def remove_address(request, address_id):
    user = request.user
    shipping_address = get_object_or_404(
        CustomerShipping, customer=user.customer, id=address_id)

    other_objects = CustomerShipping.objects.filter(
        customer=user.customer).exclude(id=address_id)

    if (shipping_address.predetermined == True and other_objects.exists()):
        random_object = other_objects[0]
        random_object.predetermined = True
        random_object.save()

    shipping_address.delete()

    return redirect("client_addresses")


@login_required
def client_orders(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    orders = Order.objects.filter(
        customer=request.user.customer, complete=True)

    context = {"orders": orders, "cartItems": cartItems}

    return render(request, 'client_orders.html', context)
