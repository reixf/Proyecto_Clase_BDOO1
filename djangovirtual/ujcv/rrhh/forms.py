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