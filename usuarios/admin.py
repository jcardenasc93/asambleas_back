from django.contrib import admin
from .models import Asambleista, Apoderado, Usuario
# Register your models here.
models = [Asambleista, Apoderado, Usuario]

admin.site.register(models)