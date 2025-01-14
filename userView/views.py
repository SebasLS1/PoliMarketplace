from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from publish.models import Producto

@login_required
def userView(request):
    user = request.user
    user_articles = Producto.objects.filter(usuario=user)
    context = {
        'name': f"{user.first_name} {user.last_name}",
        'sector': user.sector.name,
        'user_articles': user_articles,
    }
    return render(request, 'userView/userView.html', context)