# Generated by Django 3.0 on 2020-05-19 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_apoderado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apoderado',
            name='asambleista',
        ),
        migrations.AddField(
            model_name='apoderado',
            name='representa_a',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='representa_a', to='usuarios.Asambleista'),
        ),
        migrations.AddField(
            model_name='apoderado',
            name='representado_por',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Asambleista'),
        ),
    ]
