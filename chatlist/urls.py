from django.urls import path
from .views import chats_vendedor, chats_comprador

urlpatterns = [
    path('vendedor/', chats_vendedor, name='chats_vendedor'),
    path('comprador/', chats_comprador, name='chats_comprador'),
]