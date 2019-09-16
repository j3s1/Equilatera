from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from encuesta.models import Preguntas, Respuestas, Cuestionario, Organizaciones
from .serializers import CuestionarioSerializer, RespuestasSerializer
from rest_framework.parsers import JSONParser
import io, json

def index(request):
    return HttpResponse("hello")
    

class CuestionarioViewSet(viewsets.ModelViewSet):
    queryset = Cuestionario.objects.all()
    serializer_class = CuestionarioSerializer
    
    def list_cuestionario(self, request, pk=None):
        return Response(serializer_class.data)
        
class RespuestasViewSet(viewsets.ModelViewSet):
    queryset = Respuestas.objects.all()
    serializer_class = RespuestasSerializer
    def resp(self, request, pk=None):
        if serializer_class.is_valid():
            serializer_class.validated_data
        return Response(serializer_class.data)
        

