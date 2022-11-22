from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Sum, FloatField


# Create your models here.


class usuarios(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    apellidos = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    celular = models.CharField(max_length=10, null=True, blank=True)
    contraseña = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
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
    bolas_helado = models.CharField(max_length=1, null=True, blank=True)
    tipo_carne = models.CharField(max_length=1, null=True, blank=True)
    corte_pizza = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + str(self.nombrep)

    class Meta:
        ordering = ["id"]


class shelados(models.Model):
    nombres = models.CharField(max_length=25)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + " " + str(self.nombres)

    class Meta:
        ordering = ["id"]


class spizza(models.Model):
    nombres = models.CharField(max_length=25)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + " " + str(self.nombres)

    class Meta:
        ordering = ["id"]


class Pedido(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_ped = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de  {self.producto.nombrep}'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'lineapedido'
        verbose_name_plural = 'lineapedidos'
        ordering = ['id']
