from django.apps import AppConfig


class PresupuestoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.Presupuesto'

    def ready(self):
        import Models.Presupuesto.Presupuesto
