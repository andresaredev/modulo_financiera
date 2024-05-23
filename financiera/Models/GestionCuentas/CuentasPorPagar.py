from django.db import models

class CuentasPorPagar(models.Model):
    id_cuenta_pp = models.AutoField(primary_key=True)
    numero_factura = models.IntegerField()
    monto_pendiente = models.IntegerField()
    fecha_vencimiento = models.DateTimeField() 
    proveedor_debe = models.CharField(max_length=50)
    estado = models.BooleanField(default=False)
    id_transaccion = models.IntegerField()

    class Meta:
        db_table = 'cuentas_por_pagar'

    def __str__(self):
        return f"Cuenntas por pagar {self.id_cuenta_pp}"