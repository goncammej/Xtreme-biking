from .models import Product, Rating
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.views.generic.base import View
from django.http import HttpResponse
from django import forms

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comment', 'title', 'email']

def home(request):
    # Retrieve the products of each category ordered by the rating field of the rating model
    products_mountain = Product.objects.filter(category='Bicleta de montaña').order_by('-rating__rating')[:1]
    products_urban = Product.objects.filter(category='Bicicleta urbana').order_by('-rating__rating')[:1]
    products_road = Product.objects.filter(category='Bicicleta de carretera').order_by('-rating__rating')[:1]
    
    # Pass the products to the template
    context = {'products_mountain': products_mountain}
    context['products_urban'] = products_urban
    context['products_road'] = products_road
    
    return render(request, 'home.html', context)

def bike_catalogue(request):
    products_mountain = Product.objects.filter(category='Bicleta de montaña')
    products_urban = Product.objects.filter(category='Bicicleta urbana')
    products_road = Product.objects.filter(category='Bicicleta de carretera')
    
    # Pass the products to the template
    context = {'products_mountain': products_mountain}
    context['products_urban'] = products_urban
    context['products_road'] = products_road
    
    return render(request, 'bike_catalogue.html', context)

def accessories_catalogue(request):
    accssories = Product.objects.filter(category='Accesorio')
    
    # Pass the products to the template
    context = {'accessories': accssories}
    
    return render(request, 'accessories_catalogue.html', context)



def product_details(request, producto_id):
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

