from django.urls import path
from . import views

app__name = 'guardados'
urlpatterns = [
    path('', views.productos_guardados, name='guardados'),
]
