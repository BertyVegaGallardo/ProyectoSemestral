from django.contrib import admin
from .models import Formulario_Bicicletas, Formulario_disciplina, Formulario_Persona

# Register your models here.

admin.site.register(Formulario_Bicicletas)
admin.site.register(Formulario_disciplina)
admin.site.register(Formulario_Persona)