from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Evento, PreguntaAbierta, PreguntaDecimal, PreguntaMultiple, OpcionesMultiple, Documentos


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = '__all__'


class PregAbiertaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreguntaAbierta
        fields = '__all__'


class PregDecimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreguntaDecimal
        fields = '__all__'


class OpcionMultipleSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpcionesMultiple
        fields = '__all__'


class PregMultipleSerializer(serializers.ModelSerializer):
    opciones = OpcionMultipleSerializer(read_only=True, many=True)
    class Meta:
        model = PreguntaMultiple
        fields = '__all__'


class DocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documentos
        fields = '__all__'