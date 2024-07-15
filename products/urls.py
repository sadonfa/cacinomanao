from django.urls import path
from . import views

urlpatterns = [
     path('productos', views.products, name="products"),
]