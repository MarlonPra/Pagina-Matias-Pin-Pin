from django.contrib import admin
from .models import usuarios, producto, shelados, spizza

# Register your models here.


class usuariosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(usuarios, usuariosAdmin)

admin.site.register(producto)

admin.site.register(shelados)

admin.site.register(spizza)
