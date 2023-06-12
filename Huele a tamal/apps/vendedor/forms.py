from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "vendedor", "producto", "cantidad"
        widgets = {
            "vendedor": forms.Select(attrs={'class': 'form-control'}),
            "producto": forms.Select(attrs={'class': 'form-control'}),
            "cantidad": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
        }