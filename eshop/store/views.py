from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import HttpResponse
from store.forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/details.html', {'product':product})

def catalog(request):
    products = Product.objects.all()
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