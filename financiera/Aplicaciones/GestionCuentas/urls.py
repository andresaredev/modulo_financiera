from django.urls import path
from . import views

urlpatterns = [
    path('prueba', views.prueba, name='Prueba'),
    path('obtener', views.obtener, name='Obtener'),
    path('crear', views.crear, name='Crear'),
]