from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models, forms
from django.shortcuts import render


# Create your views here.


class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("Productos:index")

class ProductoList(ListView):
    model = models.Producto
    template_name = "Productos/producto_list.html"
    context_object_name = "productos"

class ProductoDelete(DeleteView):
    model = models.Producto
    template_name = "Productos/confirm_delete.html"  #esto es para colocarle cualquier nombre al template
    success_url = reverse_lazy("Productos:index")

class ProductoUpdate(UpdateView):
    model = models.Producto
    success_url = reverse_lazy("Productos:index")
    form_class = forms.ProductoForm

class ProductoDetail(DetailView):
    model = models.Producto



   