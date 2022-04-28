"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy
from store.views import index, product_detail, catalog, aboutUs, contact
from cart.views import add_to_cart, checkout, payment, payment_done
from django.conf.urls.static import static
from eshop import settings
from accounts.views import signUp, signIn, logout_user
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', index, name='index'),
    path('administration/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='admin'),
    path('admin/', admin.site.urls),
    path('signup/', signUp, name='signup'),
    path('signin/', signIn, name='signin'),
    path('logout/', logout_user, name='logout'),
    path('catalog/', catalog, name='catalog'),
    path('aboutUs/', aboutUs, name='aboutUs'),
    path('contact/', contact, name='contact'),
    path('product/<str:slug>', product_detail, name='product'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
    path('payment_done/', payment_done, name='payment_done'),
    path('add-to-cart/<int:product_id>', add_to_cart, name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
