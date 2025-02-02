from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Chat, ChatMessage
from django.shortcuts import get_object_or_404
from asgiref.sync import sync_to_async

online_users = set()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']
        self.chatroom = await sync_to_async(get_object_or_404)(Chat, chat_name=self.room_name)

        # Add user to online users set
        online_users.add(self.user.id)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Notify group about user status
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_status',
                'user_id': self.user.id,
                'status': 'online'
            }
        )

    async def disconnect(self, close_code):
        # Remove user from online users set
        online_users.discard(self.user.id)

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Notify group about user status
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_status',
                'user_id': self.user.id,
                'status': 'offline'
            }
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save message to database
        chat_message = await sync_to_async(ChatMessage.objects.create)(
            body=message,
            author=self.user,
            group=self.chatroom
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author': self.user.first_name,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        author = event['author']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'author': author,
        }))

    async def user_status(self, event):
        user_id = event['user_id']
        status = event['status']

        # Send user status to WebSocket
        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'status': status,
        }))