from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, ChatMessage
from .forms import ChatmessageCreateForm

@login_required
def chat_view(request):
    chat = get_object_or_404(Chat, chat_name='prueba')
    chat_messages = chat.chat_messages.all()[:30]
    form = ChatmessageCreateForm()
    
    if request.method == 'POST':
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user  # Asignar el autor del mensaje
            message.group = chat  # Asignar el chat al mensaje
            message.save()
            if request.headers.get('HX-Request'):
                context = {
                    'message': message,
                    'user': request.user
                }
                return render(request, 'chat/partials/chat_message_p.html', context)
            return redirect('chat_view')  # Redirigir para evitar reenvío de formulario
    else:
        form = ChatmessageCreateForm()
    
    return render(request, 'chat/chat.html', {'chat': chat, 'messages': chat_messages, 'form': form})