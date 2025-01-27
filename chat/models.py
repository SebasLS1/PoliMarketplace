from django.db import models
from django.conf import settings

# Create your models here.
class Chat(models.Model):
    chat_name = models.CharField(max_length=128, unique=True)
    
    def __str__(self):
        return self.chat_name
    
class ChatMessage(models.Model):
    group = models.ForeignKey(Chat, related_name= 'chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author.email} en {self.group.chat_name}: {self.body}'
    
    class Meta:
        ordering = ['-created_at']