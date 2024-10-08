# Generated by Django 5.1.1 on 2024-10-07 16:09

import AppEstacionaPlus.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEstacionaPlus', '0002_alter_a_funcionario_numero_identificacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='a_funcionario',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=AppEstacionaPlus.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='a_funcionario',
            name='turno',
            field=models.CharField(choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite')], max_length=5),
        ),
    ]
