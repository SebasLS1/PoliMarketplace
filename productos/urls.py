from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.producto_detalle, name='producto_detalle'),
]
