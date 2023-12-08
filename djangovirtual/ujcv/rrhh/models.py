from django.db import models

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
    identidad = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    DeptoId = models.ForeignKey(departamentos,null=True,blank=False,on_delete=models.PROTECT)
    puestoId = models.ForeignKey(puestos,null=True,blank=False,on_delete=models.PROTECT)

    def __str__(self):
        return self.identidad+''+self.nombre+''+self.apellido