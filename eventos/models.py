from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=300, null=False)
    fecha = models.DateTimeField(null=False)
    bodyCorreo = models.CharField(max_length=3000, null=False)
    linkEvento = models.CharField(max_length=300, null=False, unique=True)

    def __str__(self):
        return self.nombre