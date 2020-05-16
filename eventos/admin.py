from django.contrib import admin
from .models import Evento, PreguntaAbierta, PreguntaMultiple, OpcionesMultiple
# Register your models here.
Models = [Evento, PreguntaAbierta, PreguntaMultiple, OpcionesMultiple]
admin.site.register(Models)