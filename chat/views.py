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
            message.author = request.user  
            message.group = chat  
            message.save()
            return redirect('/chat/')  
        
        form = ChatmessageCreateForm()
    
    return render(request, 'chat/chat.html', {'chat': chat, 'messages': chat_messages, 'form': form})