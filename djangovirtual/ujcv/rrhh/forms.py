from django import forms
from .models import *

class FormEmpleado(forms.ModelForm):
    class Meta:
        model = expediente
        fields = '__all__'


class FormPuestos(forms.ModelForm):
    class Meta:
        model = puestos
        fields = '__all__'
        widgets = {
            'PuestoNombre': forms.TextInput(attrs={'class': 'form-control','required':True}),
        }

class FormDepartamentos(forms.ModelForm):
    class Meta:
        model = puestos
        fields = '__all__'
        widgets = {
            'DeptoNombre': forms.TextInput(attrs={'class': 'form-control','required':True}),
        }

