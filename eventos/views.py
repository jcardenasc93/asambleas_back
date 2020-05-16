from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .seriaizers import EventoSerializer, PregAbiertaSerializer, PregDecimalSerializer
from .models import Evento, PreguntaAbierta, PreguntaDecimal


class ListEventosView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = EventoSerializer

    def get_queryset(self):
        # check if request.user is staff
        if self.request.user.is_staff:
            return Evento.objects.all()
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        # check if request.user is staff
        if self.request.user.is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, pk=None):
        # check if request.user is staff
        if self.request.user.is_staff:
            evento = get_object_or_404(Evento, id=pk)
            evento_serializer = EventoSerializer(evento)
            return Response({'evento': evento_serializer.data})
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None, **kwargs):
        evento = get_object_or_404(Evento, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            partial = kwargs.pop('partial', False)
            serializer = EventoSerializer(
                evento, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk):
        evento = get_object_or_404(Evento, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            self.perform_destroy(evento)
            return Response({'detail': 'Evento eliminado'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)


class ListPregAbiertaView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PregAbiertaSerializer

    def get_queryset(self):
        # check if request.user is staff
        if self.request.user.is_staff:
            return PreguntaAbierta.objects.all()
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        # check if request.user is staff
        if self.request.user.is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, pk=None):
        pregunta = get_object_or_404(PreguntaAbierta, id=pk)
        pregunta_serializer = PregAbiertaSerializer(pregunta)
        return Response({'pregunta_abierta': pregunta_serializer.data})

    def retrieveByEvent(self, request, pk=None):        
        pregunta = PreguntaAbierta.objects.filter(evento=pk)
        pregunta_serializer = PregAbiertaSerializer(pregunta, many=True)
        return Response({'pregunta_abierta': pregunta_serializer.data})

    def update(self, request, pk=None, **kwargs):
        pregunta = get_object_or_404(PreguntaAbierta, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            partial = kwargs.pop('partial', False)
            serializer = PregAbiertaSerializer(
                pregunta, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk):
        pregunta = get_object_or_404(PreguntaAbierta, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            self.perform_destroy(pregunta)
            return Response({'detail': 'Pregunta eliminada'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)


class ListPregDecimalView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PregDecimalSerializer

    def get_queryset(self):
        # check if request.user is staff
        if self.request.user.is_staff:
            return PreguntaDecimal.objects.all()
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        # check if request.user is staff
        if self.request.user.is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, pk=None):
        pregunta = get_object_or_404(PreguntaDecimal, id=pk)
        pregunta_serializer = PregDecimalSerializer(pregunta)
        return Response({'pregunta_decimal': pregunta_serializer.data})

    def retrieveByEvent(self, request, pk=None):        
        pregunta = PreguntaDecimal.objects.filter(evento=pk)
        pregunta_serializer = PregDecimalSerializer(pregunta, many=True)
        return Response({'pregunta_decimal': pregunta_serializer.data})

    def update(self, request, pk=None, **kwargs):
        pregunta = get_object_or_404(PreguntaDecimal, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            partial = kwargs.pop('partial', False)
            serializer = PregDecimalSerializer(
                pregunta, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk):
        pregunta = get_object_or_404(PreguntaDecimal, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            self.perform_destroy(pregunta)
            return Response({'detail': 'Pregunta eliminada'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)
