from django.shortcuts import render
from publish.models import Producto

def main_page_view(request):
    user = request.user
    if user.is_authenticated:
        productos_sector = Producto.objects.filter(sector=user.sector).exclude(usuario=user)
        otros_productos = Producto.objects.exclude(sector=user.sector).exclude(usuario=user)
    else:
        productos_sector = Producto.objects.none()
        otros_productos = Producto.objects.all()

    context = {
        'productos_sector': productos_sector,
        'otros_productos': otros_productos,
    }
    return render(request, 'mainPage/mainPage.html', context)

