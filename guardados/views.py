from django.shortcuts import render
from publish.models import Producto
from productos.models import ProductoGuardado

def productos_guardados(request):
    user = request.user
    if user.is_authenticated:
        productos_guardados = Producto.objects.filter(productoguardado__usuario=user)
    else:
        productos_guardados = Producto.objects.none()

    context = {
        'productos_guardados': productos_guardados,
    }
    return render(request, 'guardados/guardados.html', context)
