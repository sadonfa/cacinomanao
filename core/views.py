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
        id_trab = request.POST['trabajador']
        p = request.POST.getlist('prod_id')
        
        trabajador = Worker.objects.filter(id=id_trab)

        producto = []
        for  element in p:
            producto.append(Product.objects.filter(id=element))

        print(producto)
        total = []
        for p in producto:
            for e in p:
                total.append(int(e.price))
        
        valor_total = sum(total)

    return render(request, "detalles.html", {
        'title': 'Detalles de pedido',
        'productos': producto,
        'trabajador': trabajador,
        'total': valor_total
    } )

def totalpagar(request):

   

    id_trab = request.POST['trabajador']
        
    trabajador = Worker.objects.filter(id=id_trab)

    return render(request, "totalpagar.html", {
        'title': 'Total a pagar',
        'trabajador': trabajador
    })
    