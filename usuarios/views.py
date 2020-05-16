from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import openpyxl
import os
import random

from .models import Asambleista
from .serializers import AsambleistaSerializer
from eventos.models import Evento
# Create your views here.

def random_password():
    chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
    password=""
    for i in range(10):
        password += random.choice(chars)
    return password

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def createUser(request, pk=None):
    # Lectura del archivo de Excel
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    evento = Evento.objects.get(pk=pk)    
    nombre_archivo = str(evento.documento_excel)    
    excel_file = BASE_DIR + "/media/" + nombre_archivo
    wb = openpyxl.load_workbook(excel_file)
    worksheet = wb["Sheet1"]

    # Convertimos archivo en una lista
    excel_data = list()
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    excel_data.pop(0)

    usuarios_no_creados = []
    for data in excel_data:
        asambleista = ''
        username = data[2] + '_' + data[0].replace(' ', '_').lower()
        if data[6] == 'si':
            mora = True
        else:
            mora = False
        asambleista = Asambleista(inmueble=data[0], first_name=data[1],
                                    documento=data[2], email=data[3], celular=data[4], coeficiente=data[5], 
                                    mora=mora, username=username, evento_id=pk)
        asambleista.set_password(random_password())
        try:
            asambleista.save()
            # TODO: Enviar correo

        except:
            usuarios_no_creados.append(data[0])
            pass
            
    if len(usuarios_no_creados) > 0:
        return Response({'usuarios_no_creados': usuarios_no_creados},
                            status=status.HTTP_206_PARTIAL_CONTENT)
    else:
        return Response({'detail': 'Todos los usuarios se crearon correctamente'},
                           status=status.HTTP_201_CREATED)


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
