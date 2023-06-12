from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Vendedor(models.Model):
    nombre = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido = models.CharField(max_length=50)
    celular = models.TextField(max_length=50)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = ('Vendedores')

    def __str__(self):
        return f"{self.nombre.username}"
    
class Pedido(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("Productos.Producto", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.vendedor} - {self.producto} - {self.cantidad}"
    def clean(self):
        if self.cantidad > self.producto.cantidad:
            raise ValidationError("La cantidad no puede ser mayor a la disponible")

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)
