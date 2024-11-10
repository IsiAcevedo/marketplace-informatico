from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imagen = models.URLField(max_length=200, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)  # Agregamos una categoría

    def __str__(self):
        return self.nombre
