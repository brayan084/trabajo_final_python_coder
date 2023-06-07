from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import models, forms


# Create your views here.


class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("productos:index")