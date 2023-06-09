from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'unidad_de_medida', 'cantidad', 'precio', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'unidad_de_medida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unidad de medida'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),

        }