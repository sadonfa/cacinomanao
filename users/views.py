from django.shortcuts import render
from .models import User

def users(request):

    users = User.objects.all()


    return render(request, "usuarios.html", {
        'title': 'Usuarios',
        'users': users
    })
    