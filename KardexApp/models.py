from django.db import models

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, null=True, default=None)

    def __str__(self):
        return self.descripcion


class Entrega(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    codigo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0.00)

    def __str__(self):
        return (
            f"Entrega de {self.codigo} - Fecha: {self.fecha}, Cantidad: {self.cantidad}"
        )


class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    codigo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0.00)

    def __str__(self):
        return (
            f"Ingreso de {self.codigo} - Fecha: {self.fecha}, Cantidad: {self.cantidad}"
        )


class Saldo(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0.00)

    def __str__(self):
        return f"Saldo de {self.codigo} - Cantidad: {self.cantidad}"
