# Generated by Django 3.0 on 2020-05-19 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_apoderado_documento_poder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apoderado',
            name='representa_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='representa_a', to='usuarios.Asambleista'),
        ),
    ]
