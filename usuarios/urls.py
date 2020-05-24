from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    ### ASAMBLEISTAS ###
    path('api/v1/new_asam/<int:pk>', views.createUser),
    path('api/v1/asambleistas/',
         views.ListAsambleistasView.as_view({'get': 'list'}), name='list_users'),
    path('api/v1/asambleista/<int:pk>', views.ListAsambleistasView.as_view(
        {'get': 'retrieveAsambleista'}), name='get_asambleista'),
    path('api/v1/asambleistas/<int:evento>', views.ListAsambleistasView.as_view(
        {'get': 'retrieve'}), name='list_asambleistas_evento'),
    path('api/v1/asambleistas/nuevo',
         views.ListAsambleistasView.as_view({'post': 'create'}), name='crea_asambleista'),
    path('api/v1/asambleistas/actualizar/<int:pk>', views.ListAsambleistasView.as_view(
        {'patch': 'partial_update'}), name='actualiza_asambleista'),
    path('api/v1/asambleistas/eliminar/<int:pk>',
         views.ListAsambleistasView.as_view({'post': 'destroy'}), name='elimina_asambleista'),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/asambleistas/self',
         views.UsuarioView.as_view({'get': 'list'}), name='get_self_user'),

    ### APODERADOS ###
    path('api/v1/asambleistas/apoderados/',
         views.ApoderadosView.as_view({'get': 'list'}), name='get_apoderados'),
    path('api/v1/asambleistas/apoderados/nuevo/',
         views.ApoderadosView.as_view({'post': 'create'}), name='crea_apoderado'),
    path('api/v1/asambleistas/apoderado/<int:pk>',
         views.ApoderadosView.as_view({'get': 'retrieve'}), name='retrieve_apoderado'),
    path('api/v1/asambleistas/apoderados/<int:pk>',
         views.ApoderadosView.as_view({'get': 'retrieveByEvent'}), name='retrieve_apoderados'),
    path('api/v1/asambleistas/apoderados_asam/<int:pk>',
         views.ApoderadosView.as_view({'get': 'retrieveByAsam'}), name='retrieve_apoderados_asam'),
    path('api/v1/asambleistas/apoderado/actualizar/<int:pk>',
         views.ApoderadosView.as_view({'patch': 'update'}), name='actualiza_apoderado'),
    path('api/v1/asambleistas/apoderado/eliminar/<int:pk>',
         views.ApoderadosView.as_view({'delete': 'destroy'}), name='elimina_apoderado'),

    ### COEFICIENTES ###
    path('api/v1/asambleistas/caclulo_coeficientes/<int:pk>',
         views.actualizaCoeficientes, name='calculo_coeficientes'),

]
