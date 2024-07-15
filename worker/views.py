from django.shortcuts import render
from .models import Worker

# Create your views here.

def worker(request):
    
    workers = Worker.objects.all()

    return render(request, 'worker.html', {
        'title': 'Trabajadores',
        'workers': workers
    })