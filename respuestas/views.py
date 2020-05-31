from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from datetime import datetime, time

from .serializers import RespAbiertaSerializer, RespDecimalSerializer, RespOpMultipleSerializer
from .models import RespuestaAbierta, RespuestaDecimal, RespuestaOpMultiple

from usuarios.models import Asambleista
from eventos.models import PreguntaAbierta, PreguntaDecimal, PreguntaMultiple


# Create your views here.

class RespAbiertaView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RespAbiertaSerializer

    def get_queryset(self, request, pk=None):
        # check if request.user is staff
        if self.request.user.is_staff:
            respuestas = RespuestaAbierta.objects.filter(pregunta=pk)
            serializer = RespAbiertaSerializer(respuestas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        asambleista = get_object_or_404(Asambleista, id=self.request.user.id)
        respuesta_repetida = RespuestaAbierta.objects.filter(pregunta=self.request.data['pregunta']).filter(
            asambleista=asambleista.id)
        if len(respuesta_repetida) == 0:
            pregunta = get_object_or_404(
                PreguntaAbierta, id=self.request.data['pregunta'])
            if datetime.now().time() <= pregunta.time_final:
                return serializer.save(asambleista=asambleista)
            else:
                return None
        else:
            return None

    def create(self, request, *args, **kwargs):
        pregunta = get_object_or_404(
            PreguntaAbierta, id=request.data['pregunta'])
        # valida pregunta activa
        if pregunta.activa:
            if pregunta.bloquea_mora == False:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                respuesta = self.perform_create(serializer)
                if respuesta:
                    headers = self.get_success_headers(serializer.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                else:
                    return Response({'detail': 'El usuario no puede contestar la pregunta'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                asambleista = get_object_or_404(
                    Asambleista, id=self.request.user.id)
                if asambleista.mora:
                    return Response({'detail': 'El usuario no esta habilitado para contestar'}, status=status.HTTP_400_BAD_REQUEST)
                else:
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

    def destroy(self, request, pk):
        # check if request.user is staff
        if self.request.user.is_staff:
            respuestas = RespuestaAbierta.objects.filter(pregunta=pk)
            for respuesta in respuestas:
                self.perform_destroy(respuesta)
            return Response({'detail': 'Respuestas eliminadas'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)


class RespDecimalView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RespDecimalSerializer

    def get_queryset(self, request, pk=None):
        # check if request.user is staff
        if self.request.user.is_staff:
            respuestas = RespuestaDecimal.objects.filter(pregunta=pk)
            serializer = RespDecimalSerializer(respuestas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        asambleista = get_object_or_404(Asambleista, id=self.request.user.id)
        respuesta_repetida = RespuestaDecimal.objects.filter(pregunta=self.request.data['pregunta']).filter(
            asambleista=asambleista.id)
        print(len(respuesta_repetida))
        if len(respuesta_repetida) == 0:
            pregunta = get_object_or_404(
                PreguntaDecimal, id=self.request.data['pregunta'])
            if datetime.now().time() <= pregunta.time_final:
                return serializer.save(asambleista=asambleista)
            else:
                return None
        else:
            return None

    def create(self, request, *args, **kwargs):
        pregunta = get_object_or_404(
            PreguntaDecimal, id=request.data['pregunta'])
        # valida pregunta activa
        if pregunta.activa:
            if pregunta.bloquea_mora == False:
                respuesta = request.data['respuesta_decimal']
                if pregunta.minimo <= respuesta <= pregunta.maximo:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    respuesta = self.perform_create(serializer)
                    if respuesta:
                        headers = self.get_success_headers(serializer.data)
                        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                    else:
                        return Response({'detail': 'El usuario no puede contestar la pregunta'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'detail': 'El valor no esta entre los rangos min y max permitidos'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                asambleista = get_object_or_404(
                    Asambleista, id=self.request.user.id)
                if asambleista.mora:
                    return Response({'detail': 'El usuario no esta habilitado para contestar'}, status=status.HTTP_400_BAD_REQUEST)
                else:
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

    def destroy(self, request, pk):
        # check if request.user is staff
        if self.request.user.is_staff:
            respuestas = RespuestaDecimal.objects.filter(pregunta=pk)
            for respuesta in respuestas:
                self.perform_destroy(respuesta)
            return Response({'detail': 'Respuestas eliminadas'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)


class RespOpMultipleView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RespOpMultipleSerializer

    def get_queryset(self, request, pk=None):
        respuestas = RespuestaOpMultiple.objects.filter(pregunta=pk)
        serializer = RespOpMultipleSerializer(respuestas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer, maxResps, multipleResp, strictMax):
        asambleista = get_object_or_404(Asambleista, id=self.request.user.id)
        respuesta_repetida = RespuestaOpMultiple.objects.filter(pregunta=self.request.data['pregunta']).filter(
            asambleista=asambleista.id)
        print(respuesta_repetida)

        if len(respuesta_repetida) == 0:
            pregunta = get_object_or_404(
                PreguntaMultiple, id=self.request.data['pregunta'])
            if datetime.now().time() <= pregunta.time_final:
                if multipleResp:
                    opciones = self.request.data['opciones']
                    if strictMax:
                        if len(opciones) != maxResps:
                            return 1
                        else:
                            return serializer.save(asambleista=asambleista)
                    else:
                        if len(opciones) > maxResps:
                            return 1
                        else:
                            return serializer.save(asambleista=asambleista)
                else:
                    return serializer.save(asambleista=asambleista)
            else:
                return None
        else:
            return None

    def create(self, request, *args, **kwargs):
        pregunta = get_object_or_404(
            PreguntaMultiple, id=request.data['pregunta'])
        # valida pregunta activa
        if pregunta.activa:
            if pregunta.puntajeCoeficiente:
                asambleista = get_object_or_404(
                    Asambleista, id=self.request.user.id)
                request.data['coeficientes'] = asambleista.coeficiente
            else:
                request.data['coeficientes'] = 1.000
            if pregunta.bloquea_mora == False:
                maxResps = pregunta.respuestasPermitidas
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                respuesta = self.perform_create(
                    serializer, maxResps, pregunta.esMultipleResp, pregunta.strictMax)
                if respuesta:
                    if respuesta != 1:
                        headers = self.get_success_headers(serializer.data)
                        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                    else:
                        return Response({'detail': 'Cantidad de opciones seleccionadas no permitida'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'detail': 'El usuario no puede contestar la pregunta'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                asambleista = get_object_or_404(
                    Asambleista, id=self.request.user.id)
                if asambleista.mora:
                    return Response({'detail': 'El usuario no esta habilitado para contestar'}, status=status.HTTP_400_BAD_REQUEST)
                else:
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

    def destroy(self, request, pk):
        # check if request.user is staff
        if self.request.user.is_staff:
            respuestas = RespuestaOpMultiple.objects.filter(pregunta=pk)
            for respuesta in respuestas:                
                self.perform_destroy(respuesta)
            return Response({'detail': 'Respuestas eliminadas'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)
