
from django.db import models

class Campaña(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    campaña = models.ForeignKey(Campaña, on_delete=models.CASCADE, related_name='actividades')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_programada = models.DateTimeField()
    evidencia_foto = models.ImageField(upload_to='evidencias/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.campaña.nombre}"