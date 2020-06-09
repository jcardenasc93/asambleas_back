# Generated by Django 3.0 on 2020-06-08 02:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0026_auto_20200603_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='documento',
            field=models.FileField(upload_to='docs_evento', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'jpeg', 'JPEG', 'jpg', 'JPG', 'png', 'PNG', 'mp4', 'MP4', 'mov', 'MOV'])], verbose_name='file'),
        ),
    ]
