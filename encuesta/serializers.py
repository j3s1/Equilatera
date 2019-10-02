from encuesta.models import  Preguntas, Respuestas, Organizaciones #CONSULTAR
from rest_framework import serializers

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = ('descripcion', 'id', 'tipo', 'activo', 'opciones')

class RespuestasSerializer(serializers.ModelSerializer):
    preguntaR = serializers.PrimaryKeyRelatedField(read_only=True)
    preguntas = PreguntasSerializer(many=True,read_only = True)
    #preguntasId = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Respuestas
        fields = ('descripcion', 'id', 'preguntaR','preguntas')
    #    fields = ('descripcion', 'id', 'preguntasId','preguntas')

    def create(self, validated_data):
        return Respuestas(**validated_data)

class OrganizacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizaciones
        fields = ('nombre','id','uuid','cantidad_empleado')

   

"""class OrganizacionSerializer(serializers.ModelSerializer):
    # uuid = serializers.CharField(read_only=True)

    class Meta:
        model = Organizaciones
        fields = ('id', 'nombre', 'uuid')
        extra_kwargs = {
            'uuid': {'read_only': True}
        }
 """