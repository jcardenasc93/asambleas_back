# Generated by Django 3.0 on 2020-05-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_asambleista_tiene_representante'),
    ]

    operations = [
        migrations.AddField(
            model_name='apoderado',
            name='validado',
            field=models.BooleanField(default=False),
        ),
    ]
