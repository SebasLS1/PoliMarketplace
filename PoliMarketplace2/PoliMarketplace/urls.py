from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  
    path('login/', include('login.urls')),
    path('signup/', include('signup.urls')),
    path('mainPage/', include('mainPage.urls')),
    path('userView/', include('userView.urls')),
    path('publish/', include('publish.urls')),
    path('guardados/', include('guardados.urls')),
    path('productos/', include(('productos.urls','productos'))),
    path('chat/', include('chat.urls')),
    path('chatlist/', include('chatlist.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)