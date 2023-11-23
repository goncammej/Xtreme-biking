from .models import Product, Rating
from django.db.models import Avg
from django.views.generic.base import View
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.http import JsonResponse


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def frontpage(request):
    # Retrieve the products ordered by the mean of their ratings
    featured_products = Product.objects.annotate(mean_rating=Avg('rating__rating')).order_by('-mean_rating')[:10]
    
    # Pass the products to the template
    context = {'featured_products': featured_products}
    
    return render(request, 'frontpage.html', context)

def product_list(request):
    products_mountain = Product.objects.filter(category='Bicicleta de montaña')
    products_urban = Product.objects.filter(category='Bicicleta urbana')
    products_road = Product.objects.filter(category='Bicicleta de carretera')
    accessories = Product.objects.filter(category='Accesorio')
    
    # Pass the products to the template
    context = {'products_mountain': products_mountain}
    context['products_urban'] = products_urban
    context['products_road'] = products_road
    context['accessories'] = accessories
    
    return render(request, 'product_list.html', context)


def product_details(request, producto_id):
    product = get_object_or_404(Product, pk=producto_id)
    ratings_count = product.rating_set.count()
    ratings_mean = product.rating_set.aggregate(Avg('rating'))['rating__avg']
    ratings = product.rating_set.all()
    
    context = {'product': product}
    context['ratings_count'] = ratings_count
    context['ratings_mean'] = ratings_mean
    context['ratings'] = ratings
    return render(request, 'product_details.html', context)

        
def create_rating(request, producto_id):
    if request.method == 'POST':
        rating = int(request.POST.get('selectedStars') or 0)
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        email = request.POST.get('email')
      
        product = Product.objects.get(pk=producto_id)

        new_rating = Rating.objects.create(
            bike=product,
            rating=rating,
            title=title,
            comment=comment,
            email=email
        )
        new_rating.save()
        return redirect('product_details', producto_id=producto_id)
    
    product = Product.objects.get(pk=producto_id)
    return render(request, 'rating_form.html', {'product': product})


 
def buscar_productos(request):
    if request.method == 'GET' and 'search' in request.GET:
        search_term = request.GET.get('search', '').lower()
        # Realiza la búsqueda en la base de datos
        # Filtra los productos por el término de búsqueda
        products = Product.objects.filter(title__icontains=search_term)
        # Serializa los datos de los productos para enviarlos como respuesta
        serialized_products = [{'title': product.title} for product in products]
        return JsonResponse({'products': serialized_products})
    else:
        return JsonResponse({'error': 'No se proporcionó un término de búsqueda válido'})

