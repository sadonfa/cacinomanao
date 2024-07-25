from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name="inicio"),
     path('home', views.index, name="home"),
     path('search', views.search , name="buscar"),
     path('detalles', views.detail, name="detail"),
     path('pagar', views.totalpagar, name="pagar"),
]