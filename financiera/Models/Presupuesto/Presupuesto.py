from django.db import models

class Presupuesto(models.Model):
    id_presupuesto = models.IntegerField(primary_key=True)
    año_fisacal = models.DateTimeField()
    cantidad_asignada = models.IntegerField()
    cantidad_gastada = models.IntegerField()

    class Meta:
        db_table = 'presupuesto'

    def __str__(self):
        return f"Presupuesto {self.id_presupuesto}"