# Generated by Django 5.0.6 on 2024-09-17 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('idOrganizador', models.AutoField(db_column='idOrganizador', primary_key=True, serialize=False, verbose_name='idOrganizador')),
                ('nom', models.CharField(max_length=45, verbose_name='nombre')),
                ('contacto', models.IntegerField(max_length=20, verbose_name='contacto')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('idEvento', models.AutoField(db_column='idEvento', primary_key=True, serialize=False, verbose_name='idEvento')),
                ('nom', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('fecha', models.DateField(verbose_name='Fecha de Evento')),
                ('ubicacion', models.CharField(max_length=20, verbose_name='Ubicacion')),
                ('idOrganizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.organizador', verbose_name='idOrganizador')),
            ],
        ),
    ]
