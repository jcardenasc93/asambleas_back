# Generated by Django 3.0 on 2020-05-21 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0014_apoderado_sumado'),
        ('respuestas', '0002_auto_20200521_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='asambleista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asambleista', to='usuarios.Asambleista'),
        ),
    ]
