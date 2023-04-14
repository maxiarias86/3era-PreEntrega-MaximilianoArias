from django.db import models

# Create your models here.

class Paciente(models.Model):
    DNI= models.IntegerField(unique=True)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    mail=models.EmailField(unique=True)
    fecha_nacimiento=models.DateField()
    sexo=models.CharField(max_length=20)
    
    def __str__(self):
        return f'Paciente {self.nombre} {self.apellido}, DNI {self.DNI}'

class Medico(models.Model):
    MN= models.IntegerField(unique=True)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    mail=models.EmailField(unique=True)

    def __str__(self):
        return f'Dr. {self.apellido}, {self.nombre}, MN: {self.MN}'

class Ecografia(models.Model):
    fecha_estudio=models.DateField()
    medico=models.ForeignKey(Medico, null=True, blank=True, on_delete=models.SET_NULL)
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE)
    DBP=models.FloatField()
    CC=models.FloatField()
    CA=models.FloatField()
    LF=models.FloatField()
    PFE=models.IntegerField()