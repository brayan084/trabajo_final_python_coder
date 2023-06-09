from django.db import models
from django.utils import timezone

# Create your models here.

class categoria_medidas(models.Model):

    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    
class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    unidad_de_medida = models.ForeignKey(categoria_medidas, on_delete=models.SET_NULL, null=True )
    cantidad = models.FloatField(max_length=1000)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")


    def __str__(self):
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio:.2f}"
    