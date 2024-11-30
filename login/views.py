from django.shortcuts import render, redirect
from django.contrib import messages
from signup.models import Usuario
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Intentando iniciar sesión con email: {email} y contraseña: {password}")  # Verifica que esté recibiendo los datos

        try:
            usuario = Usuario.objects.get(email=email)
            print(f"Usuario encontrado: {usuario}")  # Verifica que el usuario esté siendo encontrado en la base de datos

            if check_password(password, usuario.password):
                print("Contraseña correcta")  # Verifica que la contraseña esté siendo verificada correctamente
                login(request, usuario)
                return redirect('mainPage')  # Redirige a la página principal
            else:
                # Si la contraseña es incorrecta
                print("Contraseña incorrecta")  # Verifica que el mensaje se imprima si la contraseña es incorrecta
                messages.error(request, "Email o contraseña incorrectos. Intenta de nuevo.")
        except Usuario.DoesNotExist:
            # Si el email no está registrado
            print("Usuario no encontrado")  # Verifica que se imprima este mensaje si el usuario no está en la base de datos
            messages.error(request, "Email o contraseña incorrectos. Intenta de nuevo.")
    
    return render(request, 'login/login.html')


# Vista de Home
def home_view(request):
    return render(request, 'home/home.html')  # El template de la página de inicio
