from django.contrib import admin
from .models import Asambleista, Apoderado
# Register your models here.
models = [Asambleista, Apoderado]
admin.site.register(models)