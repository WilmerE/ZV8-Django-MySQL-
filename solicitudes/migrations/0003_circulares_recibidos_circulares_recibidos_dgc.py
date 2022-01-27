# Generated by Django 4.0.1 on 2022-01-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_circulares_dgc_alter_circulares_despachadas_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circulares_Recibidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_circ', models.CharField(max_length=10, verbose_name='No. Circular')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('dirigido', models.TextField(max_length=500, verbose_name='Dirigido')),
                ('resumen', models.TextField(max_length=500, verbose_name='Resumen')),
                ('fecha_recibido', models.DateTimeField(auto_now_add=True)),
                ('nota', models.TextField(max_length=500, verbose_name='Nota')),
            ],
            options={
                'verbose_name': 'Circular Recibido',
                'verbose_name_plural': 'Circulares Recibidos',
                'db_table': 'circ_rec',
            },
        ),
        migrations.CreateModel(
            name='Circulares_Recibidos_DGC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_circ', models.CharField(max_length=10, verbose_name='No. Circular')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('dirigido', models.TextField(max_length=500, verbose_name='Dirigido')),
                ('resumen', models.TextField(max_length=500, verbose_name='Resumen')),
                ('fecha_recibido', models.DateTimeField(auto_now_add=True)),
                ('nota', models.TextField(max_length=500, verbose_name='Nota')),
            ],
            options={
                'verbose_name': 'Circular Recibido DGC',
                'verbose_name_plural': 'Circulares Recibidos DGC',
                'db_table': 'circ_rec_dgc',
            },
        ),
    ]
