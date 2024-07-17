from django.db import models

# Create your models here.


class Worker(models.Model):
    dni = models.CharField(max_length=100, unique=True, verbose_name="dni")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=150, verbose_name="Apellidos")
    phone = models.CharField(max_length=100, verbose_name="telefono")
    cargo = models.CharField(max_length=100, verbose_name="cargo")
    contratista = models.CharField(max_length=100, verbose_name="Contratista")

    def __str__(self):
        return self.dni
