from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from encuesta.models import Preguntas, Respuestas,Organizaciones
from .serializers import  RespuestasSerializer,OrganizacionesSerializer
from rest_framework.parsers import JSONParser
import io, json

def index(request):
    return HttpResponse("hello")    
     
class RespuestasViewSet(viewsets.ModelViewSet):
    queryset = Respuestas.objects.all()
    serializer_class = RespuestasSerializer
    def resp(self, request, pk=None):
        if serializer_class.is_valid():
            serializer_class.validated_data
        return Response(serializer_class.data)
        
class OrganizacionesViewSet(viewsets.ModelViewSet):
    queryset = Organizaciones.objects.all()
    serializer_class = OrganizacionesSerializer
    def resp(self, request, pk=None):
        if serializer_class.is_valid():
            serializer_class.validated_data
        return Response(serializer_class.data)
