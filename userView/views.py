from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def userView(request):
    user= request.user
    context={
        'name':f"{user.first_name} {user.last_name}",
        'sector':user.sector.name,
    }
    return render(request, 'userView/userView.html', context)
