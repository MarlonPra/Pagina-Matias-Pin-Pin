from django.contrib import admin
from .models import usuarios, producto

# Register your models here.


class usuariosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(usuarios, usuariosAdmin)

admin.site.register(producto)
