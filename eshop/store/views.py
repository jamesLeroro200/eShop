from django.shortcuts import render, get_object_or_404, redirect, reverse
from store.models import Product, Cart, Order
from django.http import HttpResponse
from django.db.models import Q
from store.forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/details.html', {'product':product})

def catalog(request):
    products = Product.objects.all()
    query = request.GET.get('q', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'store/catalog.html', {"products": products})

def aboutUs(request):
    return render(request, 'store/aboutUs.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            do_something_with_form_data(form.cleaned_data)
            return render(request, 'store/contact_form_confirm.html')
    else:
        form = ContactForm()
    return render(request, 'store/contact.html', {
        'contact_form': form,
    })


#Vue relative à la gestion du pannier
def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)

    #1er cas : l'order n'est pas encore present dans le pannier, on le rajoute
    if created:
        cart.orders.add(order)
        #on sauvegarde le pannier
        cart.save()
    #2e cas : l'order existe déjà dans le panier, alors on incrémente juste la Qté
    else:
        order.quantity += 1
        #on sauvegarde le nouvel etat de l'order
        order.save()

    return render(request, 'store/menu_cart.html')