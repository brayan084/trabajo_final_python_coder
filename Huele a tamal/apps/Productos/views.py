from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Productos

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("Productos:producto_list")

class ProductoList(LoginRequiredMixin, ListView):
    model = models.Producto
    template_name = "Productos/producto_list.html"
    context_object_name = "productos"

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = models.Producto
    template_name = "Productos/confirm_delete.html"  #esto es para colocarle cualquier nombre al template
    success_url = reverse_lazy("Productos:index")

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = models.Producto
    success_url = reverse_lazy("Productos:index")
    form_class = forms.ProductoForm

class ProductoDetail(LoginRequiredMixin, DetailView):
    model = models.Producto

# Categorias

class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = models.categoria_medidas
    form_class = forms.CategoriaForm
    template_name = "Productos/categoria_medidas.html"
    success_url = reverse_lazy("Productos:producto_list")

class CategoriaList(LoginRequiredMixin, ListView):
    model = models.categoria_medidas
    template_name = "Productos/categoria_list.html"
    context_object_name = "categorias"

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.categoria_medidas
    template_name = "Productos/confirm_delete.html" 
    success_url = reverse_lazy("Productos:producto_list")



   