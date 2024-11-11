from django.shortcuts import render
from base_app.models import Producto

def index(request):
    productos_recientes = Producto.objects.all()[:6]  # Para el Carrousel, 6  productos más recientes
        ## TODO: Que hace a una categoria popular? Que es una categoria? Asumiendo por ahora los datos del Navbar 
    categorias_populares = Producto.objects.values('id_cate').distinct()[:4]  # 
    productos_descuento = Producto.objects.filter(descuento__isnull=False)[:8]  # Ejemplo: productos con descuento

    context = {
        'productos_recientes_start': productos_recientes[:3],
        'productos_recientes_end': productos_recientes[3:],
        'categorias_populares': categorias_populares,
        'productos_descuento': productos_descuento,
    }
    return render(request, 'index.html', context)

def productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'productos.html', context)

def detalle_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    context = {
        'producto': producto,
    }
    return render(request, 'detalle_producto.html', context)

def publicar(request):
    ### TODO: Cambiar nombre?
    return render(request, 'publicar.html')

def perfil_cliente(request):
    return render(request, 'perfil/perfil_cliente.html')

def perfil_usuario(request):
    return render(request, 'perfil/perfil_usuario.html')

def editar_perfil_view(request):
    return render (request, 'perfil/editar_perfil.html')