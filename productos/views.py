from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from publish.models import Producto, Imagen
from django.shortcuts import get_object_or_404


def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/perfilProducto.html', {'producto': producto})