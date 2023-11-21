from django.shortcuts import render, get_object_or_404

from .models import Order

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def order_details(request):
    return render(request, 'orders_details.html')

def logout(request):
    return render(request, 'logout.html')

def incident(request):
    return render(request, 'incident.html')


