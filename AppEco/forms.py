from django import forms
from AppEco.models import Medico,Paciente

generos = [
    ('M', 'masculino'),
    ('F', 'femenino'),
    ('NB', 'no binario')
]

class PacienteFormulario(forms.Form):
    
    DNI= forms.IntegerField()
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    mail=forms.EmailField()
    fecha_nacimiento=forms.DateField()
    sexo=forms.ChoiceField(choices=generos, required=True, label='Seleccione su genero')

class FormNuevaEcografia(forms.Form):
    fecha_estudio=forms.DateField()
    medico=forms.ModelChoiceField(queryset=Medico.objects.all())
    paciente=forms.ModelChoiceField(queryset=Paciente.objects.all())
    DBP=forms.FloatField()
    CC=forms.FloatField()
    CA=forms.FloatField()
    LF=forms.FloatField()
    PFE=forms.IntegerField()

class MedicoFormulario(forms.Form):
    MN= forms.IntegerField()
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    mail=forms.EmailField()