from django.db import models
from django.core.validators import FileExtensionValidator
import os
# Create your models here.


excel_validator = ['csv']


class Evento(models.Model):
    nombre = models.CharField(max_length=300, null=False)
    fecha = models.DateField(null=False)
    bodyCorreo = models.CharField(max_length=3000, null=False)
    linkEvento = models.CharField(max_length=300, null=False)
    documento_excel = models.FileField(
        upload_to='docs_excel/', validators=[FileExtensionValidator(allowed_extensions=excel_validator)], null=True)
    regitroQuorum = models.BooleanField(default=False)
    quorum = models.DecimalField(default=0.0, max_digits=25, decimal_places=3)

    @property
    def filename(self):
        return os.path.basename(self.documento_excel.name)

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    enunciado = models.CharField(max_length=500, null=False)
    activa = models.BooleanField(default=True)
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, related_name='evento')
    bloquea_mora = models.BooleanField(default=False)
    numeracion = models.BooleanField(default=False)


class PreguntaAbierta(Pregunta):
    def __str__(self):
        return self.evento.nombre + '-- ' + self.enunciado


class PreguntaDecimal(Pregunta):
    minimo = models.IntegerField(verbose_name='valor_minimo')
    maximo = models.IntegerField(verbose_name='valor_maximo')

    def __str__(self):
        return self.evento.nombre + '-- ' + self.enunciado


class PreguntaMultiple(Pregunta):
    puntajeCoeficiente = models.BooleanField(default=False)
    esMultipleResp = models.BooleanField(default=False)
    respuestasPermitidas = models.IntegerField(blank=False, default=1)
    strictMax = models.BooleanField(default=False)
    opPresentacion = models.IntegerField()

    def __str__(self):
        return self.evento.nombre + '-- ' + self.enunciado


class OpcionesMultiple(models.Model):
    opcion = models.CharField(max_length=500)
    preguntaSeleccionMultiple = models.ForeignKey(
        PreguntaMultiple, on_delete=models.CASCADE, related_name='opciones')
