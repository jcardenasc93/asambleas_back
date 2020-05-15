from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Usuario(AbstractUser):
    def __str__(self):
        return self.username + ' - ' + self.first_name


class Asambleista(Usuario):
    inmueble = models.CharField(max_length=80, blank=True, null=True)
    coeficiente = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)    
    documento = models.CharField(max_length=20, blank=True, null=True)
    celular = PhoneNumberField(null=True, blank=False)
    mora = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'asambleista'
        verbose_name_plural = 'asambleistas'

    def __str__(self):
        return self.inmueble + ' - ' + self.first_name
