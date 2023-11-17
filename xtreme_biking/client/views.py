from django.shortcuts import render

from .models import Order

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def logout(request):
    return render(request, 'logout.html')
