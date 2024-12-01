from django.urls import path
from . import views

urlpatterns = [
    path('', views.userView, name='userView'),  
]
