from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    #### RESP ABIERTA ####
    path('api/v1/respuesta/abierta/<int:pk>',
         views.RespAbiertaView.as_view({'get': 'get_queryset'}), name='list_resp_abierta'),
    path('api/v1/respuesta/abierta/nuevo/',
         views.RespAbiertaView.as_view({'post': 'create'}), name='crea_resp_abierta'),

    #### RESP DECIMAL ####
    path('api/v1/respuesta/decimal/<int:pk>',
         views.RespDecimalView.as_view({'get': 'get_queryset'}), name='list_resp_decimal'),
    # path('api/v1/respuesta/decimal/<int:pk>',
    #     views.RespDecimalView.as_view({'get': 'retrieveByPregunta'}), name='list_resp_decimal_preg'),
    path('api/v1/respuesta/decimal/nuevo/',
         views.RespDecimalView.as_view({'post': 'create'}), name='crea_resp_decimal'),
    
    #### RESP MULTIPLE ####
    path('api/v1/respuesta/op_multiple/<int:pk>',
         views.RespOpMultipleView.as_view({'get': 'get_queryset'}), name='list_resp_multiple'),
    # path('api/v1/respuesta/decimal/<int:pk>',
    #     views.RespDecimalView.as_view({'get': 'retrieveByPregunta'}), name='list_resp_decimal_preg'),
    path('api/v1/respuesta/op_multiple/nuevo/',
         views.RespOpMultipleView.as_view({'post': 'create'}), name='crea_resp_multiple'),
         
]
