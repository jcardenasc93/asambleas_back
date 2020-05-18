from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

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
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'asambleista'
        verbose_name_plural = 'asambleistas'

    def __str__(self):
        return self.inmueble + ' - ' + self.first_name
