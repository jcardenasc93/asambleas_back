from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Asambleista, Apoderado


class ApoderadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoderado        
        fields = '__all__'

class AsambleistaSerializer(serializers.ModelSerializer):
    apoderados = ApoderadosSerializer(read_only=True, many=True)
    class Meta:
        model = Asambleista
        fields = '__all__'
    
    def create(self, validated_data):
        user = Asambleista.objects.create_user(**validated_data)
        return user
