from django.db import models

class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    monto = models.IntegerField()
    tipo_transaccion = models.CharField(max_length=50)
    id_cliente = models.IntegerField()
    id_presupuesto = models.IntegerField()
    id_activo_fijo = models.IntegerField()
    id_informe = models.IntegerField()

    class Meta:
        db_table = 'transaccion'

    def __str__(self):
        return f"Transaccion {self.id_transaccion}"