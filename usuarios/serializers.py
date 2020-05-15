from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Asambleista


class AsambleistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asambleista
        fields = '__all__'
    
    def create(self, validated_data):
        user = Asambleista.objects.create_user(**validated_data)
        return user
