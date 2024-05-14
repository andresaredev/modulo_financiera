from django.apps import AppConfig


class InformeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.Informe'

    def ready(self):
        import Models.Informe.InformeFinanciero
