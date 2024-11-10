from django.shortcuts import render
from base_app.models import Producto

def index(request):
    productos_recientes = Producto.objects.all()[:8]  # Ejemplo: los 8 productos más recientes
    categorias_populares = Producto.objects.values('categoria').distinct()[:4]  # Ejemplo: 4 categorías populares
    productos_descuento = Producto.objects.filter(descuento__isnull=False)[:8]  # Ejemplo: productos con descuento

    context = {
        'productos_recientes': productos_recientes,
        'categorias_populares': categorias_populares,
        'productos_descuento': productos_descuento,
    }
    return render(request, 'index.html', context)


