"""
URL configuration for ujcv2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
#from .import views 
from .views import *


urlpatterns = [
    #path('', views.expediente_index, name='index'),
    path('', EmpleadosListar.as_view(), name='EmpleadosListar'),
    path('agregar', EmpleadosAgregar.as_view(), name='Empleadosagregar'),
    path('editar/<int:pk>/', EmpleadosEditar.as_view(), name='Empleadoseditar'),
    path('eliminar/<int:pk>/', EmpleadosEliminar.as_view(), name='Empleadoseliminar'),
    #puestos

    path('', PuestosListar.as_view(), name='puestosListar'),  
    #no tienen html 
    path('PuestosAgregar', PuestosAgregar.as_view(), name='PuestosAgregar'),
    
]   
