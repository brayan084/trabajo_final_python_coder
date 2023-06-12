from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path("pedido/", views.ventaCreate.as_view(), name="venta_create"),
    path("pedidoList/", views.ventaList.as_view(), name="venta_list"),
]