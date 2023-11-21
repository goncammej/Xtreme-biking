
from django.shortcuts import render

def frontpage(request):
    return render(request, 'frontpage.html')

def about(request):
    return render(request, 'about.html')

def product_list(request):
    return render(request, 'product_list.html')

def product_details(request):
    return render(request, 'product_details.html')
