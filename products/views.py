from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):

    products = Product.objects.all()

    return render(request, 'products.html', {
        'title': 'Productos',
        'products': products
    })