from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from encuesta.models import Preguntas, Respuestas,Organizaciones
from .serializers import  RespuestasSerializer,OrganizacionesSerializer, PreguntasSerializer
from rest_framework.parsers import JSONParser
import io, json
from django_filters.rest_framework import DjangoFilterBackend

def index(request):
    return HttpResponse("hello")    


class PreguntasViewSet(viewsets.ModelViewSet):
    queryset = Preguntas.objects.all()
    serializer_class = PreguntasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo_Usuario',]
    
 #   @link()
    #def list_preg_por_tipo(self, request, *args, **kwargs):
     #   tipo_user = self.get_object()
      #  preg_query = Preguntas.objects.filter(activo=True, tipo_Usuario=tipo_user)
       # schedule_json = PreguntasSerializer(preg_query)
        #if serializer_class.is_valid():
         #   serializer_class.validated_data
        #return Response(serializer_class.data)


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
