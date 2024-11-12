from django.shortcuts import render
from django.http import HttpResponseRedirect

from base_app.models import Producto, Categoria, Marca, Condicion_Producto
from base_app.forms import PublicarProductoForm

def index(request):
    productos_recientes = Producto.objects.all()[:6]  # Para el Carrousel, 6  productos más recientes
    productos_descuento = Producto.objects.filter(descuento__isnull=False)[:8]  # Ejemplo: productos con descuento

    context = {
        'productos_recientes_start': productos_recientes[:3],
        'productos_recientes_end': productos_recientes[3:],
        'productos_descuento_start': productos_descuento[4:],
        'productos_descuento_end': productos_descuento[:4],  
    }
    return render(request, 'index.html', context)

def productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'productos.html', context)
def productos_filtrados(request, categoria):
    categoriaProducto = Categoria.objects.get(nom_cate=categoria)
    productos = Producto.objects.filter(id_cate=categoriaProducto).all()
    context = {
        'productos': productos,
    }
    return render(request, 'productos.html', context)

def detalle_producto(request, id):
    producto = Producto.objects.get(id_prod=id)
    context = {
        'producto': producto,
    }
    return render(request, 'detalle_prod.html', context)

def publicar(request):
    if request.method == 'POST':
        form = PublicarProductoForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            producto = Producto.objects.create({
                'nombre':form.cleaned_data['nombre'] ,
                'descripcion': form.cleaned_data['descripcion'],
                'precio': form.cleaned_data['precio'],
                'descuento': form.cleaned_data['descuento'],
                'imagen': form.cleaned_data['imagen'],
                'id_mar': form.cleaned_data['marca'],
                'id_cate': form.cleaned_data['categoria'],
                'id_cond': form.cleaned_data['condicion_producto'],  
            })

            print(f'Producto {producto["nombre"]} creado.')
            return HttpResponseRedirect("/productos")
    else:
        form = PublicarProductoForm()

        categorias = Categoria.objects.all()
        marcas = Marca.objects.all()
        condiciones = Condicion_Producto.objects.all()

        context = {
            'categorias': categorias,
            'marcas': marcas,
            'condiciones': condiciones,
            'form': form,
        }
        return render(request, 'publicar.html', context)

def perfil_cliente(request):
    return render(request, 'perfil/perfil_cliente.html')

def perfil_usuario(request):
    return render(request, 'perfil/perfil_usuario.html')

def editar_perfil_view(request):
    return render (request, 'perfil/editar_perfil.html')