from django.urls import path
from . import views

urlpatterns = [
     path('categorias', views.categories, name="categories"),
]