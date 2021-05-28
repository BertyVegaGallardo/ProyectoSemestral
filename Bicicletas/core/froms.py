from django import forms
from django.forms import ModelForm
from .models import Formulario_Persona


class PersonaForm(ModelForm):

    class Meta:
        model = Formulario_Persona
        fields = '__all__'