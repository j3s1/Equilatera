from django.db import models
#from model_utilis import Choices

# Create your models here.

class Organizaciones(models.Model):
    razon=models.CharField(max_length=200)
    cantidad_empleado=models.IntegerField(default=0)

class Cuestionario(models.Model):
    fecha = models.DateField()
    encuestado = models.ForeignKey(Organizaciones, on_delete=models.CASCADE)
    
class Preguntas(models.Model):
#    OPCIONES = ['Primario', 'Secundario', 'Terciario', 'Universitario']
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE, related_name='preguntas')
    descripcion = models.TextField(max_length=500)
    fecha = models.DateField()
    tipo = models.TextField(max_length=50)
    opciones = models.TextField(blank=True)
    activo = models.BooleanField()





class Respuestas(models.Model):
    descripcion=models.TextField(max_length=500)
    fecha = models.DateField()
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)

