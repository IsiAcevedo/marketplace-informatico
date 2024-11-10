from django.contrib import admin
from django.urls import path
from TALLER_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ruta para la página principal
]
