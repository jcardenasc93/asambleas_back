# Generated by Django 3.0 on 2020-05-22 00:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0009_auto_20200521_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='documento_excel',
            field=models.FileField(null=True, upload_to='docs_excel/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])]),
        ),
    ]
