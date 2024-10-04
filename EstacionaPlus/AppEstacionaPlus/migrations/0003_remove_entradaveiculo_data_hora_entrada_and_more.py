# Generated by Django 5.1.1 on 2024-10-04 20:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEstacionaPlus', '0002_remove_entradaveiculo_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradaveiculo',
            name='data_hora_entrada',
        ),
        migrations.RemoveField(
            model_name='saidaveiculo',
            name='data_hora_saida',
        ),
        migrations.AddField(
            model_name='entradaveiculo',
            name='data_entrada',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='entradaveiculo',
            name='hora_entrada',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='saidaveiculo',
            name='data_saida',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='saidaveiculo',
            name='hora_saida',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
