from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms
from django.urls import reverse_lazy


# Create your views here.

class ventaCreate(LoginRequiredMixin, CreateView):
    model = models.Pedido
    form_class = forms.PedidoForm
    template_name = "vendedor/ventaCreate.html"
    success_url = reverse_lazy("vendedor:venta_list")

class ventaList(LoginRequiredMixin, ListView):
    model = models.Pedido
    context_object_name = "pedidos"
    template_name = "vendedor/venta_List.html"
