from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, ChatMessage
from .forms import ChatmessageCreateForm
from productos.models import Producto

@login_required
def chat_view(request, chat_name):
    chat = get_object_or_404(Chat, chat_name=chat_name)
    chat_messages = chat.chat_messages.all()[:30]
    form = ChatmessageCreateForm()
    
    return render(request, 'chat/chat.html', {'chat': chat, 'messages': chat_messages, 'form': form})

@login_required
def iniciar_chat(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    vendedor = producto.usuario
    usuario = request.user

    # Busca un chat existente entre los usuarios o crea uno nuevo
    chat, created = Chat.objects.get_or_create(
        chat_name=f'chat_{usuario.id}_{vendedor.id}',
        defaults={'title': producto.titulo}
    )
    chat.participants.add(usuario, vendedor)

    return redirect('chat_view', chat_name=chat.chat_name)