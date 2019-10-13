from encuesta.models import  Preguntas, Respuestas, Organizaciones #CONSULTAR
from rest_framework import serializers

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = ('descripcion', 'id', 'tipo', 'opciones', 'tipo_Usuario')


class OrganizacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizaciones
        fields = ('nombre','id','uuid', 'cantidad_empleado')

class RespuestasSerializer(serializers.ModelSerializer):
    organizacion_uuid = serializers.CharField(write_only=True)
    class Meta:
        model = Respuestas
        fields = ('descripcion', 'id','organizacion_uuid','pregunta')
    def create(self, validated_data):
        org = Organizaciones.objects.get(uuid=validated_data['organizacion_uuid'])
        print (validated_data['pregunta'] )
        res = Respuestas.objects.create(
            descripcion =  validated_data['descripcion'],
            pregunta = validated_data['pregunta'],
            organizacion= org, 
           
        )
        return res


