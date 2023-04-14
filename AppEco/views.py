from django.shortcuts import render
from django.http import HttpResponse
from AppEco.models import Paciente, Medico, Ecografia
from AppEco.forms import *

# Create your views here.

def inicio(request):
    return render (request, 'AppEco/inicio.html')

def pacientes(request):
    if request.method == "POST":
        form = PacienteFormulario(request.POST)
        if form.is_valid():
            paciente=Paciente()
            paciente.DNI= form.cleaned_data ['DNI']
            paciente.nombre=form.cleaned_data ['nombre']
            paciente.apellido=form.cleaned_data ['apellido']
            paciente.mail=form.cleaned_data ['mail']
            paciente.fecha_nacimiento=form.cleaned_data ['fecha_nacimiento']
            paciente.sexo=form.cleaned_data ['sexo']
            paciente.save()
            form=PacienteFormulario()
    else:
        form=PacienteFormulario()
        
    pacientes=Paciente.objects.all()

    return render (request, 'AppEco/pacientes.html', {'pacientes': pacientes, 'form':form})

def medicos(request):
    if request.method == "POST":
        form = MedicoFormulario(request.POST)
        if form.is_valid():
            medico=Medico()
            medico.MN= form.cleaned_data ['MN']
            medico.nombre=form.cleaned_data ['nombre']
            medico.apellido=form.cleaned_data ['apellido']
            medico.mail=form.cleaned_data ['mail']
            medico.save()
            form=MedicoFormulario()
    else:
        form=MedicoFormulario()
        
    medicos=Medico.objects.all()

    return render (request, 'AppEco/medicos.html', {'medicos':medicos, 'form':form})

def ecografias(request):
    return render (request, 'AppEco/ecografias.html')

def pacienteFormulario(request):
    if request.method == "POST":
        form = PacienteFormulario(request.POST)
        print(form)

        if form.is_valid():
            informacion = form.cleaned_data
        
            dni= informacion['DNI']
            nombre= informacion['nombre']
            apellido= informacion['apellido']
            mail= informacion['mail']
            fecha_nacimiento= informacion['fecha_nacimiento']
            sexo= informacion['sexo']

            paciente=Paciente(DNI=dni, nombre=nombre, apellido=apellido, mail=mail, fecha_nacimiento=fecha_nacimiento,sexo=sexo)
            paciente.save()
            return render(request, "AppEco/inicio.html")
        else:
            form=PacienteFormulario()
            mensaje= "Hubo un error en los datos ingresados (recuerde completar las fechas en formato mm/dd/aaaa)"
            return render(request, "AppEco/pacienteFormulario.html",{"form":form,"mensaje":mensaje})            
    
    else:
        form=PacienteFormulario()
        return render(request, "AppEco/pacienteFormulario.html",{"form":form})

def medicoFormulario(request):
    if request.method == "POST":
        form = MedicoFormulario(request.POST)
        print(form)

        if form.is_valid:
            informacion = form.cleaned_data
        
            mn= informacion['MN']
            nombre= informacion['nombre']
            apellido= informacion['apellido']
            mail= informacion['mail']
            
            medico=Medico(MN=mn, nombre=nombre, apellido=apellido, mail=mail)
            medico.save()
            return render(request, "AppEco/inicio.html")
    
    else:
        form=MedicoFormulario()
        return render(request, "AppEco/medicoFormulario.html",{"form":form})

def busquedaPaciente(request):
    return render(request, "AppEco/busquedaPaciente.html")
    
def buscar(request):
    try:
        DNI = request.GET["DNI"]
    except KeyError:
        return render(request, "AppEco/busquedaPaciente.html", {"mensaje": "Ingrese el DNI del paciente a buscar"})

    if DNI!="":
        pacientes = Paciente.objects.filter(DNI__icontains=DNI)
        if len(pacientes) == 0:
            mensaje = f"No se encontraron pacientes con DNI {DNI}"
            return render(request, "AppEco/resultadosBusqueda.html", {"mensaje": mensaje})
        else:
            return render(request, "AppEco/resultadosBusqueda.html", {"pacientes": pacientes})
    else:
        return render(request, "AppEco/busquedaPaciente.html", {"mensaje": "Ingrese el DNI del paciente a buscar"})

def busquedaMedico(request):
    return render(request, "AppEco/busquedaMedico.html")
    
def buscarMedico(request):
    try:
        mn = request.GET["MN"]
    except KeyError:
        return render(request, "AppEco/busquedaMedico.html", {"mensaje": "Ingrese la Matricula Nacional del médico a buscar"})

    if mn!="":
        medicos = Medico.objects.filter(MN__icontains=mn)
        if len(medicos) == 0:
            mensaje = f"No se encontraron médicos con matricula {mn}"
            return render(request, "AppEco/resultadosBusquedaMedico.html", {"mensaje": mensaje})
        else:
            return render(request, "AppEco/resultadosBusquedaMedico.html", {"medicos": medicos})
    else:
        return render(request, "AppEco/busquedaMedico.html", {"mensaje": "Ingrese la MN del paciente a buscar"})

def ecografiaFormulario(request):
    if request.method=="POST":
        form = FormNuevaEcografia(request.POST)
        print(form)

        if form.is_valid():
            informacion = form.cleaned_data
        
            fecha_estudio= informacion['fecha_estudio']
            medico=informacion['medico']
            paciente=informacion['paciente']
            DBP=informacion['DBP']
            CC=informacion['CC']
            CA=informacion['CA']
            LF=informacion['LF']
            PFE=informacion['PFE']

            ecografia=Ecografia(fecha_estudio=fecha_estudio, medico=medico, paciente=paciente, DBP=DBP, CC=CC, CA=CA, LF=LF, PFE=PFE)
            ecografia.save()
            return render(request, "AppEco/inicio.html")
    
    else:
        form=FormNuevaEcografia()
        return render(request, "AppEco/ecografiaFormulario.html",{"form":form})

def busquedaEcografia(request):
    return render(request, "AppEco/busquedaEcografia.html")
    
def buscarEcografia(request):
    try:
        paciente = request.GET["id"]
    except KeyError:
        return render(request, "AppEco/busquedaEcografia.html", {"mensaje": "Ingrese el ID del paciente a buscar"})

    if paciente!="":
        pacientes = Ecografia.objects.filter(paciente__id__icontains=int(paciente))
        if len(pacientes) == 0:
            mensaje = "No se encuentra"
            return render(request, "AppEco/resultadosBusquedaEcografia.html", {"mensaje": mensaje})
        else:
            return render(request, "AppEco/resultadosBusquedaEcografia.html", {"pacientes": pacientes})
    else:
        return render(request, "AppEco/busquedaEcografia.html", {"mensaje": "Ingrese el ID del paciente a buscar"})