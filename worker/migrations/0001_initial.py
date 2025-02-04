# Generated by Django 5.0.6 on 2024-07-13 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.TextField(max_length=100, verbose_name='dni')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('phone', models.TextField(max_length=100, verbose_name='telefono')),
                ('cargo', models.CharField(max_length=100, verbose_name='cargo')),
                ('contratista', models.CharField(max_length=100, verbose_name='Contratista')),
            ],
        ),
    ]
