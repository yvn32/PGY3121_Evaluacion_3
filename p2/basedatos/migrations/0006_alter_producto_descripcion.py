# Generated by Django 4.0.3 on 2022-06-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0005_producto_tamano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
