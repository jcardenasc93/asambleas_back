from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Asambleista
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def createUser(request):
    asambleista = Asambleista(username='asam_test', first_name='Don asambleista Test',
                              email='asambleista@asambleista.com', inmueble='INT10 AP 301', documento='1032555678')
    asambleista.set_password('asambleas2020')
    try:
        asambleista.save()
        return Response({'detail': 'Usuario {} creado correctamente'.format(asambleista.username)},
                        status=status.HTTP_201_CREATED)
    except:
        return Response({'detail': 'No se pudo crear el usuario {}. Verifique que no este duplicado'.format(asambleista.username)},
                        status=status.HTTP_409_CONFLICT)
