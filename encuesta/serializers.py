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
    preguntaR = serializers.PrimaryKeyRelatedField(read_only=True)
    preguntas = PreguntasSerializer(many=True,read_only = True)
    organizacionR = serializers.PrimaryKeyRelatedField(read_only=True)
    organizaciones = OrganizacionesSerializer(many=False,read_only = True)
    class Meta:
        model = Respuestas
        fields = ('descripcion', 'id', 'preguntaR','preguntas', 'organizacionR', 'organizaciones')

    #def create(self, validated_data):
     #   return Respuestas(**validated_data)

"""class OrganizacionSerializer(serializers.ModelSerializer):
    # uuid = serializers.CharField(read_only=True)

    class Meta:
        model = Organizaciones
        fields = ('id', 'nombre', 'uuid')
        extra_kwargs = {
            'uuid': {'read_only': True}
        }
 """
