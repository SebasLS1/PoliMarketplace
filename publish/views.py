from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Producto, Categoria, Estado, Imagen

# Helper para obtener un objeto o lanzar un error
def get_object_or_error(model, field, value, error_message):
    obj = model.objects.filter(**{field: value}).first()
    if not obj:
        raise ValueError(error_message)
    return obj

@login_required
def publish(request):
    if request.method == 'POST':
        print("Datos enviados por el formulario:", request.POST)
        print("Archivos enviados:", request.FILES)

        try:
            # Capturar datos del formulario
            titulo = request.POST.get('titulo')
            descripcion = request.POST.get('descripcion')
            precio = float(request.POST.get('precio'))
            categoria_id = request.POST.get('categoria')
            estado_id = request.POST.get('estado')
            imagenes = request.FILES.getlist('imagenes')

            # Validar campos obligatorios
            if not titulo or not descripcion or not precio:
                raise ValueError('Todos los campos son obligatorios.')

            if not imagenes:
                raise ValueError('Debes cargar al menos una imagen.')

            # Obtener la categoría y el estado
            categoria = get_object_or_error(Categoria, 'id', categoria_id, 'Categoría inválida.')
            estado = get_object_or_error(Estado, 'id', estado_id, 'Estado inválido.')

            # Crear el producto
            producto = Producto.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                precio=precio,
                usuario=request.user,
                categoria=categoria,
                estado=estado,
            )
            print(f"Producto guardado en la base de datos: {producto.titulo} (ID: {producto.id})")

            # Asociar imágenes al producto
            for imagen in imagenes:
                Imagen.objects.create(producto=producto, imagen=imagen)
                print(f"Imagen guardada: {imagen.name} para el producto {producto.titulo}")

            # Redirigir después de guardar
            return redirect('userView')

        # Manejo de errores
        except ValueError as e:
            print(f"Error de validación: {e}")
            return render(request, 'publish/publish.html', {
                'error': str(e),
                'categorias': Categoria.objects.all(),
                'estados': Estado.objects.all(),
            })
        except IntegrityError:
            print("Error de integridad en la base de datos.")
            return render(request, 'publish/publish.html', {
                'error': 'Error al guardar los datos en la base de datos.',
                'categorias': Categoria.objects.all(),
                'estados': Estado.objects.all(),
            })
        except Exception as e:
            print(f"Error inesperado: {e}")
            return render(request, 'publish/publish.html', {
                'error': f'Ocurrió un error inesperado: {e}',
                'categorias': Categoria.objects.all(),
                'estados': Estado.objects.all(),
            })

    # Renderizar el formulario
    return render(request, 'publish/publish.html', {
        'categorias': Categoria.objects.all(),
        'estados': Estado.objects.all(),
    })
