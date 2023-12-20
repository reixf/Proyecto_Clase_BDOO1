from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, ValidationError

#validacion de sexo
def validate_sexo(value):
    if value.upper() not in ['M', 'F']:
        raise ValidationError('El sexo debe ser "M" o "F".')

# Create your models here.
class departamentos(models.Model):
    DeptoId = models.IntegerField(primary_key=True)
    DeptoNombre = models.CharField(max_length=100)

    def __str__(self):
     #return str(self.DeptoId )+' '+ self.DeptoNombre
     return  self.DeptoNombre

class puestos(models.Model):
    PuestoId = models.BigAutoField(primary_key=True)
    PuestoNombre = models.CharField(max_length=100)

    def __str__(self):
     #return str(self.PuestoId)+' '+self.PuestoNombre
     return self.PuestoNombre


class expediente(models.Model):

    identidad = models.CharField(max_length=13,validators=[
      ],null=False,editable=True,verbose_name='identidad empleado')
    
    nombre = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[A-Za-z]+$', 
                message='El nombre debe contener solo letras',
            ),
            
        ],
    )
    apellido = models.CharField(max_length=100,
        validators=[
            RegexValidator(
                regex='^[A-Za-z]+$',  # Expresión regular para permitir solo letras
                message='El nombre debe contener solo letras',
            ),
            
        ],)
    sexo = models.CharField(max_length=1,
        validators=[validate_sexo],
        verbose_name='Sexo',)
    DeptoId = models.ForeignKey(departamentos,null=True,blank=False,on_delete=models.PROTECT)
    puestoId = models.ForeignKey(puestos,null=True,blank=False,on_delete=models.PROTECT)

    def __str__(self):
        return self.identidad+''+self.nombre+''+self.apellido