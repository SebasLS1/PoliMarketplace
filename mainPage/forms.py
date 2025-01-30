from django import forms
from publish.models import Categoria, Estado

class FiltroProductoForm(forms.Form):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),  # Obtiene todas las categorías
        empty_label="Selecciona una categoría",  # Esto es el texto por defecto
        required=False  # Esto permite que no sea obligatorio seleccionar una categoría
    )
    estado= forms.ModelChoiceField(
        queryset=Estado.objects.all(),  # Obtiene todas las categorías
        empty_label="Selecciona un estado",  # Esto es el texto por defecto
        required=False  # Esto permite que no sea obligatorio seleccionar una categoría
    )


