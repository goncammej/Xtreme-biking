from django.shortcuts import render, get_object_or_404

from order.models import Order
from . import forms
from .models import CustomerPaymentMethod, CustomerShipping
from django.contrib.auth.decorators import login_required

@login_required
def client_dashboard(request):
    user = request.user
    orders = Order.objects.filter(customer=user.customer)
    payment_method = CustomerPaymentMethod.objects.get(customer=user.customer)
    shipping_address = CustomerShipping.objects.get(customer=user.customer)

    payment_form = forms.PaymentMethodForm(initial={'customer': user.customer, "method": payment_method.method})
    shipping_form = forms.ShippingAdressForm(initial={'customer': user.customer, 'address': shipping_address.address, 'city': shipping_address.city, 'state': shipping_address.state, 'zipcode': shipping_address.zipcode})
    if request.method == 'POST':
        if 'payment_info' in request.POST:
            payment_form = forms.PaymentMethodForm(request.POST, instance=payment_method)
            if payment_form.is_valid():
                payment_form.save()
        if 'shipping_info' in request.POST:
            shipping_form = forms.ShippingAdressForm(request.POST, instance=shipping_address)
            if shipping_form.is_valid():
                shipping_form.save()

    context = {"user": user, "orders": orders, "payment_method": payment_method, "shipping_address": shipping_address, 'payment_form': payment_form, 'shipping_form': shipping_form}
    return render(request, 'client_dashboard.html', context)

