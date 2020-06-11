from django.contrib import admin
from .models import Asambleista, Apoderado, AbstractUser
# Register your models here.
models = [Asambleista, Apoderado, AbstractUser]
admin.site.register(models)