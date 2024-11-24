import re
from django.db import models
from django.core.validators import MinLengthValidator
from django.forms import ValidationError

class Sector(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sector'

    def __str__(self):
        return self.name

class Usuario(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, unique=True)  # Cédula debe ser única
    email = models.EmailField(unique=True, null=True)  
    password = models.CharField(max_length=100, validators=[MinLengthValidator(8)])  # Validar longitud mínima


    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # Validación de la cédula en el modelo
    def clean(self):
        if not re.match(r'^\d{10}$', self.cedula):
            raise ValidationError({'cedula': 'La cédula debe tener 10 dígitos.'})