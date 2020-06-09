# Generated by Django 3.0 on 2020-06-02 00:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0022_evento_link_conferencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='nombre_archivo')),
                ('documento', models.FileField(upload_to='docs_evento', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'jpeg', 'JPEG', 'jpg', 'JPG', 'mp4', 'MP4', 'mov', 'MOV'])], verbose_name='file')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evento_docs', to='eventos.Evento')),
            ],
        ),
    ]
