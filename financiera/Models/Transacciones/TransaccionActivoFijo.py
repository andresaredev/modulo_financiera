from django.db import models

class TransaccionActivoFijo(models.Model):
    id_activo_fijo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    valor_original = models.IntegerField()
    fecha_adquirido = models.DateTimeField()
    vida_util = models.IntegerField()
    metodo_depreciacion = models.IntegerField()
    estado_actual = models.BooleanField(default=False)
    id_transaccion = models.IntegerField()