from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    tipo_proveedor = models.IntegerField()
    condiciones_pago = models.CharField(max_length=50)
    id_cuenta_pp = models.IntegerField()

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return f'Proveedor {self.id_proveedor}'