# Generated by Django 3.2.3 on 2021-05-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210527_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario_persona',
            name='rut',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut de la persona'),
        ),
    ]
