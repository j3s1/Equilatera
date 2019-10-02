from django.contrib import admin
from encuesta.models import Preguntas, Respuestas, Organizaciones
# Register your models here.

admin.site.register(Preguntas)
admin.site.register(Respuestas)
admin.site.register(Organizaciones)

