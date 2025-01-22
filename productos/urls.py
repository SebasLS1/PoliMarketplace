from django.urls import path
from . import views

app_name = 'productos'
urlpatterns = [
    path('<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('guardar/<int:producto_id>/', views.guardar_producto, name='guardar_producto'),
]
