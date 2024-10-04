# Generated by Django 5.1.1 on 2024-10-04 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEstacionaPlus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradaveiculo',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='saidaveiculo',
            name='cliente',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppEstacionaPlus.cliente'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='placa',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
