from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest

from store.models import Product
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def cart_view(request):
    # Obtener el carrito de la sesión
    cart = request.session.get('cart')
    # Obtener la lista de productos del carrito
    cart_items = []
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product = {'product': product, 'quantity': quantity}
        cart_items.append(product)
    
    """ cart_total = 0
    for item in cart_items:
        # Calcular el total del carrito
        product_price = get_product_price(item['id'])  # Función ficticia para obtener el precio del producto
        item['total'] = product_price * item['quantity']
        cart_total += item['total'] """
    
    context = {
        'cart_items': cart_items,
        # 'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)


@csrf_exempt
def delete_product_from_cart(request, product_id):
    # Obtener el carrito de la sesión
    cart = request.session.get('cart')
    print("----------------"+str(cart))      
    # Verificar si el producto está en el carrito
    
    if product_id in cart.keys():
        # Eliminar el producto del carrito
        del cart[product_id]
        request.session['cart'] = cart
        print("----------------"+str(cart))      
    
    return redirect('/cart')

