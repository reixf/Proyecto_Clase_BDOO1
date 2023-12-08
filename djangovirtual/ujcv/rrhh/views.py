from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

#def expediente_agregar(request):
#    return HttpResponse("vista agregar ")

#def expediente_index(request):
#    return HttpResponse("hola que tal")
    
class EmpleadosListar(generic.ListView):
    template_name = 'empleados/index.html'
    model = expediente
    context_object_name = "empleados"


class EmpleadosAgregar(generic.CreateView):
    template_name = 'empleados/agregar.html'
    model = expediente
    form_class = FormEmpleado
    success_url = reverse_lazy('EmpleadosListar')


class EmpleadosEditar(generic.UpdateView):
    template_name = 'empleados/editar.html'
    model = expediente
    #model = expediente.objects.all()
    form_class = FormEmpleado
    success_url = reverse_lazy('EmpleadosListar')


class EmpleadosEliminar(generic.DeleteView):
    template_name = 'empleados/eliminar.html'
    model = expediente
    #model = expediente.objects.all()
    #form_class = FormEmpleado
    #context_object_name = "empleadoseliminar"
    success_url = reverse_lazy('EmpleadosListar')

#clases de puestos 

class PuestosListar(generic.ListView):
    template_name = 'puestos/indexpuestos.html'
    model = puestos
    context_object_name = "empleados"


class PuestosAgregar(generic.CreateView):
    template_name = 'puestos/puestosagregar.html'
    model = expediente
    form_class = FormPuestos
    success_url = reverse_lazy('EmpleadosListar')