# Generated by Django 3.0 on 2020-05-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0016_evento_quorum'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='time_final',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='timer',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]