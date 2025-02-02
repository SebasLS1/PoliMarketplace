from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chat.models import Chat
from productos.models import Producto

@login_required
def chats_vendedor(request):
    user = request.user
    productos = Producto.objects.filter(usuario=user)
    chats = Chat.objects.filter(participants=user, producto__in=productos)
    return render(request, 'chatlist/chats_vendedor.html', {'chats': chats})

@login_required
def chats_comprador(request):
    user = request.user
    productos = Producto.objects.filter(usuario=user)
    chats = Chat.objects.filter(participants=user).exclude(producto__in=productos)
    return render(request, 'chatlist/chats_comprador.html', {'chats': chats})