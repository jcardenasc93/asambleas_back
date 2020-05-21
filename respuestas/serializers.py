from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import RespuestaAbierta, RespuestaDecimal


class RespAbiertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaAbierta
        fields = '__all__'

class RespDecimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaDecimal
        fields = '__all__'