from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .models import Asambleista
from .serializers import AsambleistaSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def createUser(request):
    # TODO: Agregar validacion de usuarios staff
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
    # def retrieve(self, request, pk=None):
    #   asambleista = get_object_or_404(Asambleista, id=pk)
    #   # check if request.user is owner
    #   if concurso.owner == self.request.user:
    #       videos = UserVideo.objects.order_by(
    #           '-upload_date').filter(concurso=pk)
    #       concurso_serializer = ConcursoSerializer(concurso)
    #       videos_serializer = VideoSerializer(videos, many=True)
    #       return Response({'concurso': concurso_serializer.data, 'videos': videos_serializer.data})
    #   else:
    #       return Response({'response': 'Owner unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

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
