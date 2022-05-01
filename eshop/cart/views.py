from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from store.models import Product

from .cart import Cart

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, 'cart/menu_cart.html')

def update_cart(request, product_id, action):
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)
    qty = cart.get_item(product_id)['quantity']

    if action == 'increment':
        cart.add(product_id, 1, True)
    elif action == 'remove':
        cart.add(product_id, -qty, True)
    else:
        cart.add(product_id, -1, True)

    quantity = cart.get_item(product_id)
    if quantity:
        quantity = quantity['quantity']

        order = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'price': product.price,
            },

            'total_price': (quantity * product.price),
            'quantity': quantity,
        }
    else:
        order = None
    response= render(request, 'cart/orders_list.html', {'order':order})
    response['HX-Trigger'] = 'update_orders_list'
    return response

def orders_list(request):
    return render(request, 'cart/menu_cart.html')

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')

def payment(request):
    return render(request, 'cart/payment.html')

def payment_done(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'cart/payment_done.html')

def hx_cart_sub_total(request):
    return render(request, 'cart/cart_total.html')
