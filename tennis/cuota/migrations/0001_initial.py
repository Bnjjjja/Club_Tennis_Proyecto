# Generated by Django 5.0.6 on 2024-09-17 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jugadores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('idCuota', models.AutoField(db_column='idCuota', primary_key=True, serialize=False, verbose_name='idCuota')),
                ('nom', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('cuotaMes', models.DateField(verbose_name='Cuota Mes')),
                ('fechap', models.DateField(verbose_name='Fecha de Pago')),
                ('importe', models.FloatField(max_length=10, verbose_name='importe')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jugadores.jugador', verbose_name='id')),
            ],
        ),
    ]
