from django.contrib import admin
from .models import Categoria, Estado, Producto, Imagen

# Registro de los modelos en el admin
admin.site.register(Categoria)
admin.site.register(Estado)
admin.site.register(Producto)
admin.site.register(Imagen)
