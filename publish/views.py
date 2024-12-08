from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Producto, Categoria, Estado, Imagen

def get_object_or_error(model, field, value, error_message):
    obj = model.objects.filter(**{field: value}).first()
    if not obj:
        raise ValueError(error_message)
    return obj

@login_required
def publish(request):
    if request.method == 'POST':
        try:
            
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            precio = float(request.POST['precio'])
            categoria_id = request.POST['categoria']
            estado_id = request.POST['estado']
            imagenes = request.FILES.getlist('imagenes')

            if not titulo or not descripcion or not precio:
                raise ValueError('Todos los campos son obligatorios.')

            if not imagenes:
                raise ValueError('Debes cargar al menos una imagen.')

            categoria = get_object_or_error(Categoria, 'id', categoria_id, 'Categoría inválida.')
            estado = get_object_or_error(Estado, 'id', estado_id, 'Estado inválido.')

            producto = Producto.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                precio=precio,
                usuario=request.user,
                categoria=categoria,
                estado=estado,
            )

            for imagen in imagenes:
                Imagen.objects.create(producto=producto, imagen=imagen)

            return redirect('userView')  
        
        except ValueError as e:
            return render(request, 'publish/publish.html', {
                'error': str(e),
                'categorias': Categoria.objects.all(),
                'estados': Estado.objects.all(),
                

            })
        except IntegrityError:
            return render(request, 'publish/publish.html', {
                'error': 'Error al guardar los datos en la base de datos.',
                'categorias': Categoria.objects.all(),
                'estados': Estado.objects.all(),
            })
        except Exception as e:
            return render(request, 'publish/publish.html', {
                'error': f'Ocurrió un error inesperado: {e}',
                'categorias': Categoria.objects.all(),
                'estados': Estado.objects.all(),

            })
    

    return render(request, 'publish/publish.html', {
        'categorias': Categoria.objects.all(),
        'estados': Estado.objects.all(),
    })

