from django.contrib import admin
from .models import Evento, PreguntaAbierta, PreguntaMultiple, OpcionesMultiple, InmueblesQuorum
# Register your models here.
Models = [Evento, PreguntaAbierta, PreguntaMultiple, OpcionesMultiple, InmueblesQuorum]
admin.site.register(Models)
