from django.apps import AppConfig


class ProveedorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.Proveedor'

    def ready(self):
        import Models.Proveedor.ProveedorModel