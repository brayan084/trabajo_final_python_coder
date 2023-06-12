from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.admin.views.decorators import staff_member_required



urlpatterns = [
    path('', TemplateView.as_view(template_name='Productos/index.html'), name='index'),
    path("create/", staff_member_required(views.ProductoCreate.as_view()), name="producto_create"),
    path("categoria/", staff_member_required(views.CategoriaCreate.as_view()), name="categoria_create"),
    path("list/", views.ProductoList.as_view(), name="producto_list"),
    path("categoria/list/", views.CategoriaList.as_view(), name="categoria_list"),
    path("deleteCategoria/<int:pk>", staff_member_required(views.CategoriaDelete.as_view()), name="categoria_delete"),
    path("deleteProducto/<int:pk>", staff_member_required(views.ProductoDelete.as_view()), name="producto_delete"),
    path("update/<int:pk>", staff_member_required(views.ProductoUpdate.as_view()), name="producto_update"),
    path("detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),

]