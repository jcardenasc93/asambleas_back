# Generated by Django 3.0 on 2020-05-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20200519_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='asambleista',
            name='tiene_representante',
            field=models.BooleanField(default=False),
        ),
    ]
