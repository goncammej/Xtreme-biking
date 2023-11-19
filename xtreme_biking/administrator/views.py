from django.shortcuts import render, get_object_or_404  

# Create your views here.

def admin_orders_details(request):
    return render(request, 'list_orders.html')

def admin_incidents_details(request):
    return render(request, 'list_incidents.html')