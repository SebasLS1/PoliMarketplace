from django.db import models
from django.conf import settings
from productos.models import Producto

class Chat(models.Model):
    chat_name = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chats')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='chats')

    def __str__(self):
        return self.chat_name

    def is_user_online(self, user):
        # Implementa la lógica para verificar si el usuario está en línea
        return user.is_authenticated and user.is_active

class ChatMessage(models.Model):
    group = models.ForeignKey(Chat, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.email} en {self.group.chat_name}: {self.body}'

    class Meta:
        ordering = ['created_at']