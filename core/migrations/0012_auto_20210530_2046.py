# Generated by Django 3.2.3 on 2021-05-31 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210527_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario_disciplina',
            name='Formulario_Bicicletas',
        ),
        migrations.AlterField(
            model_name='formulario_persona',
            name='Apellido_materno',
            field=models.CharField(max_length=40, verbose_name='apellido materno'),
        ),
        migrations.DeleteModel(
            name='Formulario_Bicicletas',
        ),
        migrations.DeleteModel(
            name='Formulario_disciplina',
        ),
    ]
