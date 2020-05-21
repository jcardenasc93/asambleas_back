from django.db import models
from eventos.models import PreguntaAbierta, PreguntaDecimal
from usuarios.models import Asambleista
# Create your models here.

class Respuesta(models.Model):
    asambleista = models.ForeignKey(Asambleista, on_delete=models.CASCADE, related_name='asambleista', null=True)
    fecha_hora = models.DateTimeField(verbose_name='fecha_hora', auto_now_add=True)

class RespuestaAbierta(Respuesta):
    pregunta = models.ForeignKey(PreguntaAbierta, on_delete=models.CASCADE, related_name='pregunta_abierta')
    respuesta_texto = models.TextField(max_length=512, blank=True, default='')

class RespuestaDecimal(Respuesta):
    pregunta = models.ForeignKey(PreguntaDecimal, on_delete=models.CASCADE, related_name='pregunta_decimal')
    respuesta_decimal = models.DecimalField(max_digits=20, decimal_places=3)
