from django.urls import path
from . import views

urlpatterns = [
    path('prueba', views.test, name='Prueba'),
    path('crear', views.crear, name='Crear'),
    path('obtener', views.obtener, name='Obtener'),
    path('actualizar/<int:id>', views.actualizar, name='Actualizar'),
    path('eliminar/<int:id>', views.eliminar, name='Actualizar'),
    path('transaccionActivoFijo/obtener', views.obtenerAF, name='Obtener'),
    path('transaccionActivoFijo/crear', views.crearAF, name='Crear'),
    path('transaccionActivoFijo/actualizar/<int:id>', views.actualizarAF, name='Actualizar'),
    path('transaccionActivoFijo/eliminar/<int:id>', views.eliminarAF, name='Actualizar'),
]