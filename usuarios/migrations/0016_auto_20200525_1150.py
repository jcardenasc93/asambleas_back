# Generated by Django 3.0 on 2020-05-25 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0015_apoderado_evento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asambleista',
            options={'ordering': ['inmueble'], 'verbose_name': 'asambleista', 'verbose_name_plural': 'asambleistas'},
        ),
    ]
