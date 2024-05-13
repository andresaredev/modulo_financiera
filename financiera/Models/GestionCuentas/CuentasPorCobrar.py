from django.db import models

class CuentasPorCobrar(models.Model):
    id_cuenta_pc = models.IntegerField(primary_key=True)
    monto_pendiente = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    id_cliente = models.IntegerField()
    id_transaccion = models.IntegerField()

    class Meta:
        db_table = 'cuenta_por_cobrar'
    
    def __str__(self):
        return f'Cuentas por cobrar {self.id_cuenta_pc}'
