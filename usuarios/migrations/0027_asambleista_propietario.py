# Generated by Django 3.0 on 2020-06-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0026_asambleista_cantidadpoderes'),
    ]

    operations = [
        migrations.AddField(
            model_name='asambleista',
            name='propietario',
            field=models.BooleanField(default=True),
        ),
    ]
