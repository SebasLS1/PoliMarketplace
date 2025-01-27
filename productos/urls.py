from django.urls import path
from . import views
from chat.views import iniciar_chat

app_name = 'productos'
urlpatterns = [
    path('<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('guardar/<int:producto_id>/', views.guardar_producto, name='guardar_producto'),
    path('iniciar_chat/<int:producto_id>/', iniciar_chat, name='iniciar_chat'),
]