from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .serializers import RespAbiertaSerializer
from .models import RespuestaAbierta

from usuarios.models import Asambleista
from eventos.models import PreguntaAbierta


# Create your views here.

class RespAbiertaView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RespAbiertaSerializer

    def get_queryset(self):
        # check if request.user is staff
        if self.request.user.is_staff:
            return RespuestaAbierta.objects.all()

    def perform_create(self, serializer):
        asambleista = get_object_or_404(Asambleista, id=self.request.user.id)
        respuesta_repetida = RespuestaAbierta.objects.filter(
            asambleista=asambleista.id)
        
        if len(respuesta_repetida) == 0:
            return serializer.save(asambleista=asambleista)
        else:
            return None

    def create(self, request, *args, **kwargs):
        pregunta = get_object_or_404(
            PreguntaAbierta, id=request.data['pregunta'])
        # valida pregunta activa
        if pregunta.activa:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            respuesta = self.perform_create(serializer)
            if respuesta:
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'detail': 'El usuario ya contestó la pregunta'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'detail': 'La pregunta no se encuentra activa'}, status=status.HTTP_400_BAD_REQUEST)
