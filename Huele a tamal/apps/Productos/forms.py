from django import forms
from .models import Producto, categoria_medidas

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria_medidas
        fields = "__all__"
        labels = {
            'nombre': '',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),

        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'unidad_de_medida': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),

        }