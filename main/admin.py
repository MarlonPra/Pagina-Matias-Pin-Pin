from django.contrib import admin
from .models import *

# Register your models here.


class usuariosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(usuarios, usuariosAdmin)

admin.site.register(producto)

admin.site.register(shelados)

admin.site.register(spizza)

admin.site.register(Pedido)

admin.site.register(LineaPedido)
