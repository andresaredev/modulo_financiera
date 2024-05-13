from django.urls import path
from . import views

urlpatterns = [
    path('prueba', views.test, name='Prueba'),
    path('crear', views.crear, name='Crear'),
    path('obtener', views.obtener, name='Obtener'),
    path('actualizar/<int:id>', views.actualizar, name='Actualizar'),
    path('eliminar/<int:id>', views.eliminar, name='Actualizar'),
]