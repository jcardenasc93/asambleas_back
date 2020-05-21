from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import RespuestaAbierta


class RespAbiertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaAbierta
        fields = '__all__'
