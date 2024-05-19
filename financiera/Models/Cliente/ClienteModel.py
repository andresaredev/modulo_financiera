from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return f"Cliente {self.id_cliente}"