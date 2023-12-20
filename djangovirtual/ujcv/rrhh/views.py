from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#def expediente_agregar(request):
#    return HttpResponse("vista agregar ")

#def expediente_index(request):
#    return HttpResponse("hola que tal")
    
class EmpleadosListar(LoginRequiredMixin,generic.ListView):
    template_name = 'empleados/index.html'
    model = expediente
    context_object_name = "empleados"
    login_url='/login/'


class EmpleadosAgregar(LoginRequiredMixin,generic.CreateView):
    template_name = 'empleados/agregar.html'
    model = expediente
    form_class = FormEmpleado
    login_url='/login/'
    success_url = reverse_lazy('EmpleadosListar')


class EmpleadosEditar(LoginRequiredMixin,generic.UpdateView):
    template_name = 'empleados/editar.html'
    model = expediente
    #model = expediente.objects.all()
    form_class = FormEmpleado
    login_url='/login/'
    success_url = reverse_lazy('EmpleadosListar')


class EmpleadosEliminar(LoginRequiredMixin,generic.DeleteView):
    template_name = 'empleados/eliminar.html'
    model = expediente
    #model = expediente.objects.all()
    #form_class = FormEmpleado
    #context_object_name = "empleadoseliminar"
    login_url='/login/'
    success_url = reverse_lazy('EmpleadosListar')

#clases de puestos 

class PuestosListar(LoginRequiredMixin,generic.ListView):
    template_name = 'puestos/indexpuestos.html'
    model = puestos
    login_url='/login/'
    context_object_name = "puestos"


class PuestosAgregar(LoginRequiredMixin,generic.CreateView):
    template_name = 'puestos/agregar.html'
    model = puestos
    form_class = FormPuestos
    login_url='/login/'
    success_url = reverse_lazy('PuestosListar')


#nohtml aun

class PuestosEditar(LoginRequiredMixin, generic.UpdateView):
    template_name = 'puestos/editar.html'
    model = puestos
    form_class = FormPuestos
    login_url='/login/'
    success_url = reverse_lazy('puestosListar')

class PuestosEliminar(LoginRequiredMixin, generic.DeleteView):
    template_name = 'puestos/eliminar.html'
    model = puestos
    login_url='/login/'
    success_url = reverse_lazy('puestosListar')
"""" 
#desde aqui no hay html
class PuestosEditar(generic.UpdateView):
    template_name = 'puestos/editar.html'
    model = puestos
    form_class = FormPuestos
    success_url = reverse_lazy('PuestosListar')


class PuestosEliminar(generic.DeleteView):
    template_name = 'puestos/eliminar.html'
    model = puestos
    success_url = reverse_lazy('PuestosListar')"""

#departamentos

def lista_departamentos(request):
    departamentos = departamentos.objects.all()
    return render(request, 'departamentos/index.html', {'departamentos': departamentos})

def crear_departamento(request):
    if request.method == 'POST':
        form = FormDepartamentos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_departamentos')  
        form = FormDepartamentos()
    return render(request, 'departamentos/agregar.html', {'form': form})
