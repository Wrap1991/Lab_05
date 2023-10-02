from django.contrib import admin
from .models import Categoria, Producto, Cliente

admin.site.register(Categoria)
admin.site.register(Producto)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'fecha_publicacion')
    list_filter = ('fecha_nacimiento',)
    search_fields = ('nombres', 'apellidos', 'dni', 'email')
    actions = ['marcar_como_importante']

    def marcar_como_importante(self, request, queryset):
        queryset.update(importante=True)

    marcar_como_importante.short_description = "Marcar como importante"




