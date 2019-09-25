from encuesta.models import Cuestionario, Preguntas, Respuestas, Organizaciones #CONSULTAR
from rest_framework import serializers

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = ('descripcion', 'id', 'tipo', 'activo', 'opciones')

class RespuestasSerializer(serializers.ModelSerializer):
    preguntaR = serializers.PrimaryKeyRelatedField(read_only=True)
    preguntas = PreguntasSerializer(read_only = True)
    #preguntasId = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Respuestas
        fields = ('descripcion', 'id', 'preguntaR', 'preguntas')
    #    fields = ('descripcion', 'id', 'preguntasId','preguntas')

    def create(self, validated_data):
        return Respuestas(**validated_data)


class CuestionarioSerializer(serializers.ModelSerializer):
    preguntas = PreguntasSerializer(many=True, read_only = True)
    respuestas = RespuestasSerializer(many=True, read_only = True)
    class Meta:
        model = Cuestionario
        fields = ('preguntas', 'respuestas', 'fecha', 'encuestado')


