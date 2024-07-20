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
    t = Worker.objects.filter(dni=dni)


    return render(request, "search.html",{
        'title': 'Generar Pedido',
        'trabajador': t,
        'productos': productos
    })

def detail(request):

    if request.method == "POST":
        p = request.POST.getlist('prod_id')

        producto = []
        for  element in p:
            producto.append(Product.objects.filter(id=element))

    return render(request, "detalles.html", {
        'title': 'Detalles de pedido',
        'productos': producto
    } )
    