import uuid
from django.db import models
#from model_utilis import Choices

# Create your models here.

class Organizaciones(models.Model):
    nombre=models.CharField(max_length=200)
    cantidad_empleado=models.IntegerField(default=0)
    uuid =models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.nombre


class Preguntas(models.Model):
    opcionesTipo =[('texto', 'texto'),('si_no', 'si_no'),('multiple', 'multiple')]
   # cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE, related_name='preguntas')
    descripcion = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, choices=opcionesTipo)
    opcionesTipoUsuario =(('rrhh', 'rrhh'), ('empleado', 'empleado'))
    tipo_Usuario = models.CharField(max_length=50, choices=opcionesTipoUsuario)
    opciones = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion


class Respuestas(models.Model):
    descripcion=models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE, related_name='preguntaR')
    organizacion = models.ForeignKey(Organizaciones, on_delete=models.CASCADE,related_name='organizacionR')

    def __str__(self):
        return f'{self.descripcion} ({self.organizacion})'
