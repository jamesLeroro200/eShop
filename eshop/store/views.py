from django.shortcuts import render, get_object_or_404, redirect, reverse
from store.models import Product, Cart, Order
from django.http import HttpResponse
from django.db.models import Q
from store.forms import ContactForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    similar_products = Product.objects.exclude(name=product.name)
    query = request.GET.get('q', product.category)

    if query:
        similar_products = similar_products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'store/details.html', {'product':product, 'suggestions':similar_products})

def catalog(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        #if page is out of range, deliver last page of results
        products = paginator.page(paginator.num_pages)

    query = request.GET.get('q', '')

    if query:
        products = products_list.filter(Q(name__icontains=query) | Q(description__icontains=query))
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
