from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('comparador.urls')),
    path('admin/', admin.site.urls),
    path('categorias', include('comparador.urls')),
]
urlpatterns += staticfiles_urlpatterns()