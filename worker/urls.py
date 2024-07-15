from django.urls import path
from . import views

urlpatterns = [
     path('trabajadores', views.worker, name="worker"),
]