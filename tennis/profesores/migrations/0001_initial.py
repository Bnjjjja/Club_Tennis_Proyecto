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
            name='Profesor',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('DNI', models.IntegerField(verbose_name='DNI')),
                ('nom', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('fechan', models.DateField(verbose_name='Fecha Nacimiento')),
                ('dire', models.CharField(max_length=50, verbose_name='Direccion')),
                ('cd', models.CharField(max_length=6, verbose_name='codigo postal')),
                ('descripcion', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='jugadores.deporte', verbose_name='descripcion')),
            ],
        ),
    ]
