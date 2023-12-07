from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from store.utils import cartData

from .forms import SignUpForm


def signup(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form, 'cartItems': cartItems})
