from django.db import models
from django.db.models.base import Model

# Create your models here.

class Formulario_Persona(models.Model):
    rut = models.CharField(max_length=9,primary_key=True, verbose_name='Rut sin punto ni guion')
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    Apellido_paterno = models.CharField(max_length=50, verbose_name='apellido paterno')
    Apellido_materno = models.CharField(max_length=50, verbose_name='apellido materno')
    edad = models.IntegerField(verbose_name='Edad ')
    sexo = models.CharField(max_length=50, verbose_name='Sexo')

    def __str__(self):
        return self.rut
        



class Formulario_Bicicletas(models.Model):
    idTipo_bicicleta = models.IntegerField(primary_key=True, verbose_name='Id tipo de bicicleta')
    tipo_bicicleta = models.CharField(max_length=70, verbose_name='Tipo de bicicleta')
    rango_edad_uso = models.CharField(max_length=30, verbose_name='Rango de la edad que pueden usar este tipo de bicicletas')

    def __str__(self):
        return self.tipo_bicicleta


class Formulario_disciplina(models.Model):
    idDisciplina = models.IntegerField(primary_key=True, verbose_name='Id de la disciplina')
    disciplina = models.CharField(max_length=70, verbose_name='Disciplina de la bicicleta')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion de la disciplina')
    Formulario_Bicicletas = models.ForeignKey(Formulario_Bicicletas, on_delete=models.CASCADE)

    def __str__(self):
        return self.disciplina