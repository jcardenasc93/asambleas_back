# Generated by Django 3.0 on 2020-06-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0021_auto_20200529_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asambleista',
            name='nombre_completo',
            field=models.CharField(default='Juan', max_length=200),
            preserve_default=False,
        ),
    ]
