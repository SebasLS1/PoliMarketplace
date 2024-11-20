from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Sector, Usuario
from django.contrib.auth.hashers import make_password

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        sector_id = request.POST.get('sector')
        cedula = request.POST.get('cedula')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not all([first_name, last_name, birth_date, gender, sector_id, cedula, password, confirm_password]):
            messages.error(request, 'Todos los campos son obligatorios.')
        elif password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
        else:
            sector = Sector.objects.get(id=sector_id)
            hashed_password = make_password(password)
            usuario = Usuario(
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                gender=gender,
                sector=sector,
                cedula=cedula,
                password=hashed_password
            )
            usuario.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('home')  # Redirige a la página de inicio o a donde desees

    sectors = Sector.objects.all()
    return render(request, 'signup/signup.html', {'sectors': sectors})