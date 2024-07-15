from django.shortcuts import render
from .models import Category

# Create your views here.

def categories(request):
    categori = Category.objects.all()

    return render(request, 'categories.html', {
        'title': 'Categorias',
        'categori': categori
    }),
