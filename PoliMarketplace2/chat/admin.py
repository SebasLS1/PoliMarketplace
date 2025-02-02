# filepath: /c:/Users/ASUS/Documents/Req/PoliMarketPlace/chat/admin.py
from django.contrib import admin
from .models import Chat, ChatMessage

class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 1

class ChatAdmin(admin.ModelAdmin):
    inlines = [ChatMessageInline]

admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatMessage)