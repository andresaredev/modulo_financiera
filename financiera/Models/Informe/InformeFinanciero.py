from django.db import models

class InformeFinanciero(models.Model):
    id_informe = models.IntegerField(primary_key=True)
    nombre_informe = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    tipo_informe = models.CharField(max_length=50)
    detalle_informe = models.CharField(max_length=50)
    nombre_responsable = models.CharField(max_length=50)
    id_transaccion_financiera = models.IntegerField()

    class Meta:
        db_table = 'informe_financiero'

    def __str__(self):
        return f'Informe financiero {self.id_informe}'