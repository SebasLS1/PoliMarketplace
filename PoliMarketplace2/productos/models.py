from django.conf import settings
from django.db import models
from publish.models import Producto  # Asegúrate de que el modelo Producto está en esta app o ajusta la importación.

class ProductoGuardado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'producto')  # Evitar duplicados de usuario-producto
        verbose_name = "Producto Guardado"
        verbose_name_plural = "Productos Guardados"

    def __str__(self):
        return f"{self.usuario.username} guardó {self.producto.titulo}"
