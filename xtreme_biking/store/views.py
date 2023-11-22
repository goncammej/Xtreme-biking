from .models import Product, Rating
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.views.generic.base import View
from django.http import HttpResponse
from django import forms
from django.shortcuts import redirect

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comment', 'title', 'email']

def about(request):
    return render(request, 'about.html')

def product_list(request):
    return render(request, 'product_list.html')

def frontpage(request):
    # Retrieve the products of each category ordered by the rating field of the rating model
    products= Product.objects.order_by('-rating__rating')[:7]
    context = {"products": products}
    
    return render(request, 'home.html', context)

def catalogue(request):
    products = Product.objects.all
    context = {"products": products}

    return render(request, 'product_list.html', context)

def product_details(request, producto_id):
    if request.method == 'POST':
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('/cart')
    else:
        product = get_object_or_404(Product, pk=producto_id)
        ratings_count = product.rating_set.count()
        ratings_mean = product.rating_set.aggregate(Avg('rating'))['rating__avg']
        
        context = {'product': product}
        context['ratings_count'] = ratings_count
        context['ratings_mean'] = ratings_mean
        return render(request, 'product_details.html', context)

def get(request, producto_id):
    product = get_object_or_404(Product, pk=producto_id)
    ratings = product.rating_set.all()

    context = {'ratings': ratings}
    context['product'] = product

    response = render(request, 'ratings.html', context)
    return HttpResponse(response)
        
def post(request, producto_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.bike = Product.objects.get(pk=producto_id)
            rating.save()
            response = render(request, 'ratings.html')
    else:
        form = RatingForm()
        response = render(request, 'rating_form.html', {'form': form})

    return HttpResponse(response)

