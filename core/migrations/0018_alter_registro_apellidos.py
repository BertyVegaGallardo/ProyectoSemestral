# Generated by Django 3.2.3 on 2021-06-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210601_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='apellidos',
            field=models.CharField(max_length=60, verbose_name='apellidos'),
        ),
    ]
