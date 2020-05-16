from django.contrib import admin
from .models import Evento, PreguntaAbierta
# Register your models here.
Models = [Evento, PreguntaAbierta]
admin.site.register(Models)