from django.db import models

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"

class Mantencion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='mantenciones')
    fecha = models.DateField()
    descripcion = models.TextField()
    costo = models.IntegerField()

    def __str__(self):
        return f"Mantención: {self.vehiculo.patente} - {self.fecha}"