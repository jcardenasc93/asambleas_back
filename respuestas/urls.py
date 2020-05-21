from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    #### RESP ABIERTA ####
    path('api/v1/respuesta/abierta',
         views.RespAbiertaView.as_view({'get': 'list'}), name='list_resp_abierta'),
    path('api/v1/respuesta/abierta/nuevo/',
         views.RespAbiertaView.as_view({'post': 'create'}), name='crea_resp_abierta'),
]
