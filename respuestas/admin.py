from django.contrib import admin
from .models import RespuestaAbierta, RespuestaDecimal, RespuestaOpMultiple
# Register your models here.

Models = [RespuestaAbierta, RespuestaDecimal, RespuestaOpMultiple]
admin.site.register(Models)
