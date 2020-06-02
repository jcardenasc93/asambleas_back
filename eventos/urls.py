from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    #### EVENTOS ####
    path('api/v1/eventos/',
         views.ListEventosView.as_view({'get': 'list'}), name='list_eventos'),
    path('api/v1/eventos/<int:pk>',
         views.ListEventosView.as_view({'get': 'retrieve'}), name='list_evento'),
    path('api/v1/eventos/nuevo',
         views.ListEventosView.as_view({'post': 'create'}), name='crea_evento'),
    path('api/v1/eventos/actualizar/<int:pk>', views.ListEventosView.as_view(
         {'patch': 'partial_update'}), name='actualiza_evento'),
    path('api/v1/eventos/eliminar/<int:pk>',
         views.ListEventosView.as_view({'post': 'destroy'}), name='elimina_evento'),

    #### PREGUNTA ABIERTA ####
    path('api/v1/eventos/pregunta_abierta/',
         views.ListPregAbiertaView.as_view({'get': 'list'}), name='list_preg_abiertas'),
    path('api/v1/eventos/pregunta_abierta/<int:pk>',
         views.ListPregAbiertaView.as_view({'get': 'retrieve'}), name='list_preg_abierta'),
    path('api/v1/eventos/pregunta_abierta/evento/<int:pk>',
         views.ListPregAbiertaView.as_view({'get': 'retrieveByEvent'}), name='list_preg_abierta_evento'),
    path('api/v1/eventos/pregunta_abierta/nuevo',
         views.ListPregAbiertaView.as_view({'post': 'create'}), name='crea_preg_abierta'),
    path('api/v1/eventos/pregunta_abierta/actualizar/<int:pk>',
         views.ListPregAbiertaView.as_view({'patch': 'partial_update'}), name='actualiza_preg_abierta'),
    path('api/v1/eventos/pregunta_abierta/eliminar/<int:pk>',
         views.ListPregAbiertaView.as_view({'post': 'destroy'}), name='elimina_preg_abierta'),


    #### PREGUNTA DECIMAL ####
    path('api/v1/eventos/pregunta_decimal/',
         views.ListPregDecimalView.as_view({'get': 'list'}), name='list_preg_decimales'),
    path('api/v1/eventos/pregunta_decimal/<int:pk>',
         views.ListPregDecimalView.as_view({'get': 'retrieve'}), name='list_preg_decimal'),
    path('api/v1/eventos/pregunta_decimal/evento/<int:pk>',
         views.ListPregDecimalView.as_view({'get': 'retrieveByEvent'}), name='list_preg_decimal_evento'),
    path('api/v1/eventos/pregunta_decimal/nuevo',
         views.ListPregDecimalView.as_view({'post': 'create'}), name='crea_preg_decimal'),
    path('api/v1/eventos/pregunta_decimal/actualizar/<int:pk>',
         views.ListPregDecimalView.as_view({'patch': 'partial_update'}), name='actualiza_preg_decimal'),
    path('api/v1/eventos/pregunta_decimal/eliminar/<int:pk>',
         views.ListPregDecimalView.as_view({'post': 'destroy'}), name='elimina_preg_decimal'),


    #### PREGUNTA MULTIPLE ####
    path('api/v1/eventos/pregunta_multiple/',
         views.ListPregMultipleView.as_view({'get': 'list'}), name='list_preg_multiple'),
    path('api/v1/eventos/pregunta_multiple/<int:pk>',
         views.ListPregMultipleView.as_view({'get': 'retrieve'}), name='list_preg_multiple'),
    path('api/v1/eventos/pregunta_multiple/evento/<int:pk>',
         views.ListPregMultipleView.as_view({'get': 'retrieveByEvent'}), name='list_preg_multiple_evento'),
    path('api/v1/eventos/pregunta_multiple/nuevo',
         views.ListPregMultipleView.as_view({'post': 'create'}), name='crea_preg_multiple'),
    path('api/v1/eventos/pregunta_multiple/actualizar/<int:pk>',
         views.ListPregMultipleView.as_view({'patch': 'partial_update'}), name='actualiza_preg_multiple'),
    path('api/v1/eventos/pregunta_multiple/eliminar/<int:pk>',
         views.ListPregMultipleView.as_view({'post': 'destroy'}), name='elimina_preg_multiple'),


    ### QUORUM ###
    path('api/v1/quorum_status/<int:pk>',
         views.solicitaQuorum, name='solicita_quorum'),
    path('api/v1/quorum_asambleista/<int:pk>',
         views.regitroQuorum, name='quorum_asambleista'),
    path('api/v1/quorum_reset/<int:pk>',
         views.reinicioQuorum, name='quorum_reset'),

    #### DOCUMENTOS ####
    path('api/v1/eventos/documentos/<int:pk>',
         views.DocumentosView.as_view({'get': 'retrieveEvent'}), name='list_docs'),
    path('api/v1/eventos/documento_nuevo',
         views.DocumentosView.as_view({'post': 'create'}), name='crea_doc'),
    path('api/v1/eventos/eliminar_documento/<int:pk>',
         views.DocumentosView.as_view({'delete': 'destroy'}), name='elimina_doc')
]
