from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("home", views.index, name="index"),
    path("productos", views.productos, name="producto"),
    path("producto/{id}", views.detalle_producto, name="detalle_producto"),
    path("publicar", views.publicar, name="publicar"),
]