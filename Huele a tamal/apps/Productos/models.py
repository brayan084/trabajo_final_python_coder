from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    unidad_de_medida = models.CharField(max_length=50)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name="descripción")
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    # class Meta:
    #     verbose_name = "producto"
    #     verbose_name_plural = "productos"

    def __str__(self):
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio:.2f}"