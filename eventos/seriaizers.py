from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = '__all__'
