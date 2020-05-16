from django.db import models
from django.core.validators import FileExtensionValidator
import os
# Create your models here.


excel_validator = ['xlsx']


class Evento(models.Model):
    nombre = models.CharField(max_length=300, null=False)
    fecha = models.DateField(null=False)
    bodyCorreo = models.CharField(max_length=3000, null=False)
    linkEvento = models.CharField(max_length=300, null=False, unique=True)
    documento_excel = models.FileField(
        upload_to='docs_excel/', validators=[FileExtensionValidator(allowed_extensions=excel_validator)], null=True)

    @property
    def filename(self):
        return os.path.basename(self.documento_excel.name)
    def __str__(self):
        return self.nombre
