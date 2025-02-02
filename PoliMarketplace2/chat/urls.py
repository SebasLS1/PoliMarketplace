from django.urls import path
from .views import chat_view, iniciar_chat

urlpatterns = [
    path('<str:chat_name>/', chat_view, name='chat_view'),
    path('iniciar_chat/<int:producto_id>/', iniciar_chat, name='iniciar_chat'),
]