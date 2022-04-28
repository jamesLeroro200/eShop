from django.shortcuts import render, redirect

from .cart import Cart

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')

def checkout(request):
    return render(request, 'cart/checkout.html')

def payment(request):
    return render(request, 'cart/payment.html')

def payment_done(request):
    return render(request, 'cart/payment_done.html')
