from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator

from eventos.models import Evento

# Create your models here.


class Usuario(AbstractUser):
    def __str__(self):
        return self.username + ' - ' + self.first_name


class Asambleista(Usuario):
    inmueble = models.CharField(max_length=80, blank=True, null=True)
    coeficiente = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    celular = PhoneNumberField(blank=True, null=True)
    mora = models.BooleanField(default=False)
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, blank=True, null=True)
    tiene_representante = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'asambleista'
        verbose_name_plural = 'asambleistas'
        ordering = ['inmueble']

    def __str__(self):
        if self.is_staff:
            return self.username
        else:
            return self.inmueble + ' - ' + self.first_name


doc_poder_ext = ['pdf', 'PDF', 'JPEG', 'JPG', 'PNG', 'png', 'jpg', 'jpeg']


class Apoderado(models.Model):
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE)
    representa_a = models.ForeignKey(
        Asambleista, on_delete=models.CASCADE, related_name='representa_a', null=True, blank=True)
    representado_por = models.ForeignKey(
        Asambleista, on_delete=models.CASCADE, null=True, related_name='representado_por')
    validado = models.BooleanField(default=False)
    documento_poder = models.FileField(upload_to='poderes/', validators=[
                                       FileExtensionValidator(allowed_extensions=doc_poder_ext)], null=False, blank=True)
    sumado = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'apoderado'
        verbose_name_plural = 'apoderados'
