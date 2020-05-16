from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
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
    path('api/v1/eventos/pregunta_abierta/',
         views.ListPregAbiertaView.as_view({'get': 'list'}), name='list_preg_abiertas'),
    path('api/v1/eventos/pregunta_abierta/<int:pk>',
         views.ListPregAbiertaView.as_view({'get': 'retrieve'}), name='list_preg_abierta'),
    path('api/v1/eventos/pregunta_abierta/nuevo',
         views.ListPregAbiertaView.as_view({'post': 'create'}), name='crea_preg_abierta'),
    path('api/v1/eventos/pregunta_abierta/actualizar/<int:pk>',
         views.ListPregAbiertaView.as_view({'patch': 'partial_update'}), name='actualiza_preg_abierta'),
    path('api/v1/eventos/pregunta_abierta/eliminar/<int:pk>',
         views.ListPregAbiertaView.as_view({'post': 'destroy'}), name='elimina_preg_abierta'),
]
