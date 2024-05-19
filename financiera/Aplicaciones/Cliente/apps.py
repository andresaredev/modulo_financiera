from django.apps import AppConfig


class ClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.Cliente'

    def ready(self):
        import Models.Cliente.ClienteModel