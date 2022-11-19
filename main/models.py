from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class usuarios(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    apellidos = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    celular = models.CharField(max_length=10, null=True, blank=True)
    contraseña = models.CharField(max_length=50, null=True, blank=True)
    TIPOS = [
        ("C", "Cliente"),
        ("A", "Asesor")]
    tipo = models.CharField(max_length=20, default='C', choices=TIPOS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.usuario)


class producto(models.Model):
    nombrep = models.CharField(max_length=200, null=True)
    tipop = [
        ("H", "Heladeria"),
        ("PZ", "Pizzeria"),
        ("CR", "Comida Rapida"),
        ("B", "Bebidas")]
    tipo = models.CharField(max_length=20, default='H', choices=tipop)
    precio = models.FloatField(blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + " " + str(self.nombrep)

    class Meta:
        ordering = ["id"]
