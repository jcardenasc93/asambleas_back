from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import xlrd
import os
import random
import boto3

from .models import Asambleista, Apoderado
from .serializers import AsambleistaSerializer, ApoderadosSerializer
from eventos.models import Evento
# Create your views here.


def random_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
    password = ""
    for i in range(10):
        password += random.choice(chars)
    return password


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def createUser(request, pk=None):
    if request.user.is_staff:
        # Lectura del archivo de Excel
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        evento = Evento.objects.get(pk=pk)
        nombre_archivo = str(evento.documento_excel)
        # Valida si existe archivo para el evento
        if nombre_archivo:
            nombre_archivo = 'media/' + nombre_archivo
            # Access to S3 bucket
            AWS_ACCESS_KEY_ID = os.environ.get(
                'BUCKETEER_AWS_ACCESS_KEY_ID', '')
            AWS_SECRET_ACCESS_KEY = os.environ.get(
                'BUCKETEER_AWS_SECRET_ACCESS_KEY', '')
            AWS_STORAGE_BUCKET_NAME = os.environ.get(
                'BUCKETEER_BUCKET_NAME', '')

            s3_session = boto3.client(service_name='s3',
                                      aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            file_obj = s3_session.get_object(
                Bucket=AWS_STORAGE_BUCKET_NAME, Key=nombre_archivo)
            excel_content = file_obj['Body'].read().decode('utf-8')

            excel_content = excel_content.split('\n')
            excel_content.pop(0)

            usuarios_no_creados = []
            for row in excel_content:    # Iterate through rows
                if row != '':
                    inmueble, nombres, documento, correo, celular, coeficiente, mora = row.split(
                        ';')
                    asambleista = ''
                    username = documento + '_' + \
                        inmueble.replace(' ', '_').lower()
                    if mora == 'si':
                        mora = True
                    else:
                        mora = False

                    asambleista = Asambleista(inmueble=inmueble, first_name=nombres,
                                              documento=documento, email=correo, celular=celular, coeficiente=float(
                                                  coeficiente),
                                              mora=mora, username=username, evento_id=pk)
                    asambleista.set_password(random_password())

                    try:
                        asambleista.save()
                        # TODO: Enviar correo

                    except:
                        usuarios_no_creados.append(inmueble)
                        pass

            if len(usuarios_no_creados) > 0:
                return Response({'usuarios_no_creados': usuarios_no_creados},
                                status=status.HTTP_206_PARTIAL_CONTENT)
            else:
                return Response({'detail': 'Todos los usuarios se crearon correctamente'},
                                status=status.HTTP_201_CREATED)

        else:
            return Response({'detail': 'No existe un archivo excel asociado al evento'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)


class ListAsambleistasView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AsambleistaSerializer

    def get_queryset(self):
        # check if request.user is staff
        if self.request.user.is_staff:
            return Asambleista.objects.all()
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

    def retrieveAsambleista(self, request, pk=None):
        # check if request.user is staff
        if self.request.user.is_staff:
            asambleista = get_object_or_404(Asambleista, id=pk)
            print(asambleista)
            asambleista_serializer = AsambleistaSerializer(
                asambleista)
            return Response({'asambleista': asambleista_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, evento=None):
        # check if request.user is staff
        if self.request.user.is_staff:
            asambleistas = Asambleista.objects.filter(evento=evento)
            asambleistas_serializer = AsambleistaSerializer(
                asambleistas, many=True)
            return Response({'asambleistas': asambleistas_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None, **kwargs):
        asambleista = get_object_or_404(Asambleista, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            partial = kwargs.pop('partial', False)
            serializer = AsambleistaSerializer(
                asambleista, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(serializer.data)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk):
        asambleista = get_object_or_404(Asambleista, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            self.perform_destroy(asambleista)
            return Response({'detail': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)


class UsuarioView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AsambleistaSerializer

    def get_queryset(self):
        return Asambleista.objects.filter(id=self.request.user.id)


class ApoderadosView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ApoderadosSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Apoderado.objects.all()
        return Apoderado.objects.filter(representado_por=self.request.user.id)

    def perform_create(self, serializer):
        asambleista = get_object_or_404(Asambleista, id=self.request.user.id)
        serializer.save(representado_por=asambleista)

    def create(self, request, pk=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apoderado = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"Apoderado creado correctamente"}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, **kwargs):
        apoderado = get_object_or_404(Apoderado, id=pk)
        representa_a = None
        try:
            representa_a = request.data['representa_a']
        except:
            pass
        # check if request.user is staff
        if self.request.user.is_staff:
            if representa_a:
                if len(Apoderado.objects.filter(representa_a=representa_a).filter(validado=True)) == 0:
                    partial = kwargs.pop('partial', False)
                    serializer = ApoderadosSerializer(
                        apoderado, data=request.data, partial=partial)
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)
                    return Response(serializer.data)
                else:
                    return Response({'detail': 'El asambleista ya cuenta con otro apoderado'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                partial = kwargs.pop('partial', False)
                serializer = ApoderadosSerializer(
                    apoderado, data=request.data, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, pk=None):
        # check if request.user is staff
        if self.request.user.is_staff:
            apoderado = Apoderado.objects.get(id=pk)
            apoderado_serializer = ApoderadosSerializer(apoderado)
            return Response({'apoderado': apoderado_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieveByEvent(self, request, pk=None):
        # check if request.user is staff
        if self.request.user.is_staff:
            apoderados = Apoderado.objects.filter(evento=pk)
            apoderados_serializer = ApoderadosSerializer(apoderados, many=True)
            return Response({'apoderados': apoderados_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def retrieveByAsam(self, request, pk=None):
        # check if request.user is staff
        if self.request.user.is_staff:
            apoderados = Apoderado.objects.filter(representado_por=pk)
            apoderados_serializer = ApoderadosSerializer(apoderados, many=True)
            return Response({'apoderados': apoderados_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk):
        apoderado = get_object_or_404(Apoderado, id=pk)
        # check if request.user is staff
        if self.request.user.is_staff:
            self.perform_destroy(apoderado)
            return Response({'detail': 'Apoderado eliminado'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Acceso denegado. Autentiquese como usuario administrador"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def actualizaCoeficientes(request, pk=None):
    if request.user.is_staff:
        asambleista = Asambleista.objects.get(id=pk)
        apoderados_validos = Apoderado.objects.filter(
            representado_por=pk).filter(validado=True)
        total_coeficiente = asambleista.coeficiente
        if len(apoderados_validos) > 0:
            for apoderado in apoderados_validos:
                if apoderado.sumado == False:
                    total_coeficiente += apoderado.representa_a.coeficiente
                    Apoderado.objects.filter(
                        id=apoderado.id).update(sumado=True)

        apoderados_no_validos = Apoderado.objects.filter(
            representado_por=pk).filter(validado=False).filter(sumado=True)
        print(apoderados_no_validos)
        if len(apoderados_no_validos) > 0:
            for apoderado in apoderados_no_validos:
                total_coeficiente -= apoderado.representa_a.coeficiente
                Apoderado.objects.filter(id=apoderado.id).update(
                    sumado=False, representa_a=None)

        Asambleista.objects.filter(id=pk).update(coeficiente=total_coeficiente)
        return Response({"nuevo_coeficiente": total_coeficiente})
