from django.apps import AppConfig


class TransaccionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.Transacciones'

    def ready(self):
        import Models.Transacciones.TransaccionModel
