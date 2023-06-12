from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Vendedor)


@admin.register(models.Pedido)
class VentaAdmin(admin.ModelAdmin):
    list_display = (
        "vendedor",
        "producto",
        "cantidad",
        "precio_total",
        "fecha_venta",
    )
    list_display_links = ("producto",)
    search_fields = ("producto.nombre", "vendedor")
    ordering = ("fecha_venta",)
    list_filter = ("vendedor",)
    date_hierarchy = "fecha_venta"