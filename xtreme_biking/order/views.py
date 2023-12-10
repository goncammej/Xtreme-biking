from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from store.utils import cartData

from .models import Order, CustomerReviews, CustomerClaims
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from . import forms

from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect


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

@login_required
def create_review(request, order_id):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user
    order = get_object_or_404(Order, customer=user.customer, id=order_id)
    review_form = forms.reviewForm(order=order)
    if request.method == 'POST':
        if 'review_info' in request.POST:
            review_form = forms.reviewForm(
                request.POST, order=order)
            if review_form.is_valid():
                review_instance = review_form.save(commit=False)
                review_instance.order = order
                review_instance.save()
                return redirect('client_orders')
    if request.method == 'GET':
        context = {"user": user, 'form': review_form, 'cartItems': cartItems}
        return render(request, 'customer_review_form.html', context)
    
@login_required
def edit_review(request, order_id):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user
    order = get_object_or_404(Order, customer=user.customer, id=order_id)
    review_instance = get_object_or_404(
        CustomerReviews, order=order)
    review_form = forms.reviewForm(initial = {'review': review_instance.review, 'order': review_instance.order})
    if request.method == 'POST':
        if 'review_info' in request.POST:
            review_form = forms.reviewForm(
                request.POST, instance=review_instance)
            if review_form.is_valid():
                review_form.save()
                return redirect('client_orders')
    if request.method == 'GET':
        context = {"user": user, "review_instance": review_instance,
                   'form': review_form, 'cartItems': cartItems}
        return render(request, 'customer_review_form.html', context)
    
@login_required
def create_claim(request, order_id):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user
    order = get_object_or_404(Order, customer=user.customer, id=order_id)
    claim_form = forms.claimForm(order=order)
    if request.method == 'POST':
        if 'claim_info' in request.POST:
            claim_form = forms.claimForm(
                request.POST, order=order)
            if claim_form.is_valid():
                claim_instance = claim_form.save(commit=False)
                claim_instance.order = order
                claim_instance.save()
                return redirect('client_orders')
    if request.method == 'GET':
        context = {'user': user, 'form': claim_form, 'cartItems': cartItems}
        return render(request, 'customer_claim_form.html', context)
    
@login_required
def edit_claim(request, order_id):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user
    order = get_object_or_404(Order, customer=user.customer, id=order_id)
    claim_instance = get_object_or_404(
        CustomerClaims, order=order)
    claim_form = forms.claimForm(initial = {'claim': claim_instance.claim, 'order': claim_instance.order})
    if request.method == 'POST':
        if 'claim_info' in request.POST:
            claim_form = forms.claimForm(
                request.POST, instance=claim_instance)
            if claim_form.is_valid():
                claim_form.save()
                return redirect('client_orders')
    if request.method == 'GET':
        context = {"user": user, "review_instance": claim_instance,
                   'form': claim_form, 'cartItems': cartItems, 'status': claim_instance.status}
        return render(request, 'customer_claim_form.html', context)
