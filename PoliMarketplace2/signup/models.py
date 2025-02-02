from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator
import re
from django.forms import ValidationError

class Sector(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sector'

    def __str__(self):
        return self.name

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, unique=True)  # Cédula debe ser única
    email = models.EmailField(unique=True, null=True)  
    password = models.CharField(max_length=100, validators=[MinLengthValidator(8)])  # Validar longitud mínima
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Validación de la cédula en el modelo
    def clean(self):
        if not re.match(r'^\d{10}$', self.cedula):
            raise ValidationError({'cedula': 'La cédula debe tener 10 dígitos.'})
