from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Sector, Usuario
from django.contrib.auth.hashers import make_password
import re

# Función para validar la edad (mayor de 18 años)
def validar_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad >= 18

# Función para validar la cédula ecuatoriana
def validar_cedula_ecuatoriana(cedula):
    if not re.match(r'^\d{10}$', cedula):
        return False
    suma = 0
    for i in range(9):
        num = int(cedula[i]) * (2 if i % 2 == 0 else 1)
        suma += num if num < 10 else num - 9

    digito_verificador = 0 if (suma % 10) == 0 else 10 - (suma % 10)
    return digito_verificador == int(cedula[9])

# Función de validación de correo electrónico
def validar_email(email):
    # Verifica que el correo no sea None y tenga un formato válido
    if email is None:
        return False
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        sector_id = request.POST.get('sector')
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        # Convertir la fecha de nacimiento
        try:
            birth_date = date.fromisoformat(birth_date)
        except ValueError:
            messages.error(request, 'Formato de fecha inválido.')

        # Validaciones (acumular todos los errores)
        error_occurred = False
        
        if not all([first_name, last_name, birth_date, gender, sector_id, cedula, email, password, confirm_password]):
            messages.error(request, 'Todos los campos son obligatorios.')
            error_occurred = True
        if len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            error_occurred = True
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            error_occurred = True
        if not validar_edad(birth_date):
            messages.error(request, 'Debes ser mayor de 18 años.')
            error_occurred = True
        if not validar_cedula_ecuatoriana(cedula):
            messages.error(request, 'Cédula inválida.')
            error_occurred = True
        if Usuario.objects.filter(cedula=cedula).exists():
            messages.error(request, 'Esta cédula ya está registrada.')
            error_occurred = True
        # Validación de correo electrónico más robusta
        if not validar_email(email):
            messages.error(request, 'Correo inválido.')
            error_occurred = True
        elif Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Correo ya registrado.')
            error_occurred = True

        if error_occurred:
            return render(request, 'signup/signup.html', {'sectors': Sector.objects.all()})

        # Si no hay errores, procesar el registro
        sector = Sector.objects.get(id=sector_id)
        hashed_password = make_password(password)
        usuario = Usuario(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            sector=sector,
            cedula=cedula,
            email=email,
            password=hashed_password
        )
        usuario.save()
        messages.success(request, 'Registro exitoso.')
        return redirect('home')
    
    sectors = Sector.objects.all()
    return render(request, 'signup/signup.html', {'sectors': sectors})