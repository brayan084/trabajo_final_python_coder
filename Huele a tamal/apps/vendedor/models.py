from django.db import models
from django.contrib.auth.models import User

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