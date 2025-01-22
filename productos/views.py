from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from productos.models import ProductoGuardado
from publish.models import Producto, Imagen
from django.shortcuts import get_object_or_404


@login_required
def guardar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    usuario = request.user

    if ProductoGuardado.objects.filter(usuario=usuario, producto=producto).exists():
        mensaje = "Este producto ya está guardado."
    else:
        ProductoGuardado.objects.create(usuario=usuario, producto=producto)
        mensaje = "Producto guardado exitosamente."

    return render(request, 'productos/perfilProducto.html', {
        'producto': producto,
        'mensaje': mensaje,
    })  

def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/perfilProducto.html', {'producto': producto})
