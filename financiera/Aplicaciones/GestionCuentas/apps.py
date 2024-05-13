from django.apps import AppConfig


class GestioncuentasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.GestionCuentas'

    def ready(self):
        import Models.GestionCuentas.CuentasPorCobrar