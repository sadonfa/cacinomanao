from django.shortcuts import render
from worker.models import Worker
from products.models import Product

# Create your views here.

def index(request):

    worker = Worker.objects.all()

    return render(request, "home.html", {
        'title': 'Inicio',
        'worker': worker
    })

def search(request):

    productos = Product.objects.all()
    dni = request.GET['buscar']
    t = Worker.objects.filter(id=1)
    print(t)

    return render(request, "search.html",{
        'title': 'Buscador',
        'trabajador': t,
        'productos': productos
    })