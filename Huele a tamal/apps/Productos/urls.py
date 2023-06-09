from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='Productos/index.html'), name='index'),
    path("create/", views.ProductoCreate.as_view(), name="producto_create"),
    path("/list/", views.ProductoList.as_view(), name="producto_list"),
    path("delete/<int:pk>", (views.ProductoDelete.as_view()), name="producto_delete"),
    path("update/<int:pk>", (views.ProductoUpdate.as_view()), name="producto_update"),
    path("detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),

]