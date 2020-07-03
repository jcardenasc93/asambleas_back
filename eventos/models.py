from django.db import models
from django.core.validators import FileExtensionValidator
import os

from django.contrib.postgres.fields import ArrayField

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
    quorum = models.DecimalField(default=0.0, max_digits=30, decimal_places=20)
    cantidadQuorum = models.IntegerField(default=0)
    logo_asamblea = models.ImageField(
        verbose_name='logo', null=True, upload_to='logos')
    link_conferencia = models.URLField(
        verbose_name='link_conferencia', null=True)
    codConferencia = models.CharField(
        max_length=150, verbose_name='codigo_conferencia', null=True)

    @property
    def filename(self):
        return os.path.basename(self.documento_excel.name)

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    enunciado = models.CharField(max_length=500, null=False)
    activa = models.BooleanField(default=False)
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, related_name='evento')
    bloquea_mora = models.BooleanField(default=False)
    numeracion = models.BooleanField(default=False)
    timer = models.IntegerField()
    time_final = models.TimeField(null=True)


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
    esMultipleResp = models.BooleanField(default=True)
    respuestasPermitidas = models.IntegerField(blank=False, default=1)
    strictMax = models.BooleanField(default=False)
    opPresentacion = models.IntegerField()

    def __str__(self):
        return self.evento.nombre + '-- ' + self.enunciado


class OpcionesMultiple(models.Model):
    opcion = models.CharField(max_length=500)
    preguntaSeleccionMultiple = models.ForeignKey(
        PreguntaMultiple, on_delete=models.CASCADE, related_name='opciones')


doc_validator = ['pdf', 'PDF', 'jpeg', 'JPEG',
                 'jpg', 'JPG', 'png', 'PNG', 'mp4', 'MP4', 'mov', 'MOV']


class Documentos(models.Model):
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, related_name='evento_docs')
    nombre = models.CharField(verbose_name='nombre_archivo', max_length=255)
    documento = models.FileField(verbose_name='file', upload_to='docs_evento', validators=[
                                 FileExtensionValidator(allowed_extensions=doc_validator)])


class Quorum(models.Model):
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, related_name='evento_quorum')
    coeficiente_total = models.DecimalField(max_digits=30, decimal_places=20)
    coeficiente_registrado = models.DecimalField(
        max_digits=30, decimal_places=20)
    date_time = models.DateTimeField(
        auto_now_add=True, verbose_name='fecha_hora_registro')
    cantidadPersonas = models.IntegerField(default=0)
    imuebles_registrados = ArrayField(models.CharField(
        null=True, max_length=4, default=''), blank=True, null=True)
