from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("home", views.index, name="index"),
    path("productos", views.productos, name="productos"),
    path("productos/<str:categoria>", views.productos_filtrados, name="productos_filtrados"),
    path("producto/<int:id>", views.detalle_producto, name="detalle_producto"),
    path("publicar", views.publicar, name="publicar"),
]