from django.urls import path
from AppEco.views import *

urlpatterns = [
    
    path("", inicio, name="inicioAppEco"),
    path("pacientes/", pacientes, name="pacientes"),
    path("medicos/", medicos, name="medicos"),
    path("ecografias/", ecografias, name="ecografias"),
    path("pacienteFormulario/", pacienteFormulario, name="pacienteFormulario"),
    path("busquedaPaciente/", busquedaPaciente, name="busquedaPaciente"),
    path('buscar/', buscar, name='buscar'),
    path('medicoFormulario/',medicoFormulario, name='medicoFormulario'),
    path("busquedaMedico/", busquedaMedico, name="busquedaMedico"),
    path('buscarMedico/', buscarMedico, name='buscarMedico'),
    path('ecografiaFormulario/', ecografiaFormulario, name='ecografiaFormulario'),
    path("busquedaEcografia/", busquedaEcografia, name="busquedaEcografia"),
    path('buscarEcografia/', buscarEcografia, name='buscarEcografia'),
    
]