from django import forms

from base_app.models import Producto, Categoria, Marca, Condicion_Producto

def get_marcas():
    return {marca.id_mar: marca.nom_mar for marca in Marca.objects.all()} 

def get_condiciones():
    return {condicion.id_cond: condicion.nom_cond for condicion in Condicion_Producto.objects.all()}

def get_categorias():
    return {categoria.id_cate: categoria.nom_cate for categoria in Categoria.objects.all()}


class PublicarProductoForm(forms.Form):    

    nombre = forms.CharField(label="nombre", max_length=50)
    descripcion = forms.CharField(label="descripcion", max_length=50)
    precio = forms.DecimalField(label="Precio", max_digits=10)
    descuento   = forms.DecimalField(label="Descuento", max_digits=2)
    ##imagen = forms.URLField(label="Imagen", max_length=200)
    ##No logro hacer Imagen funcionar
    marca = forms.ChoiceField(label="Marca", choices=get_marcas)
    categoria = forms.ChoiceField(label="Categoría", choices=get_categorias)
    condicion_producto = forms.ChoiceField(label="Condición del producto", choices=get_condiciones)
