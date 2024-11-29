
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  
    path('login/', include('login.urls')),
    path('signup/', include('signup.urls')),
    path('mainPage/', include('mainPage.urls')),
]
