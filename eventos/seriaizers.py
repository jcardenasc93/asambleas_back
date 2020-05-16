from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Evento, PreguntaAbierta, PreguntaDecimal


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
