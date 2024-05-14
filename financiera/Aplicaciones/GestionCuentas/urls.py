from django.urls import path
from . import views

urlpatterns = [
    path('prueba', views.prueba, name='Prueba'),
    path('CuentasPorCobrar/obtener', views.obtenerCC, name='Obtener'),
    path('CuentasPorCobrar/crear', views.crearCC, name='Crear'),
    path('CuentasPorCobrar/actualizar/<int:id>', views.actualizarCC, name='Actualizar'),
    path('CuentasPorCobrar/eliminar/<int:id>', views.eliminarCC, name='Eliminar'),
    path('CuentasPorPagar/obtener', views.obtenerCP, name='Obtener'),
    path('CuentasPorPagar/crear', views.crearCP, name='Crear'),
    path('CuentasPorPagar/actualizar/<int:id>', views.actualizarCP, name='Actualizar'),
    path('CuentasPorPagar/eliminar/<int:id>', views.eliminarCP, name='Eliminar'),
]