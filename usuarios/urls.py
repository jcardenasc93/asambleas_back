from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [    
    path('api/v1/new_asam/<int:pk>', views.createUser),
    path('api/v1/asambleistas/', views.ListAsambleistasView.as_view({'get': 'list'}), name='list_users'),
    path('api/v1/asambleistas/<int:evento>', views.ListAsambleistasView.as_view({'get': 'retrieve'}), name='list_asambleistas_evento'),
    path('api/v1/asambleistas/nuevo', views.ListAsambleistasView.as_view({'post': 'create'}), name='crea_asambleista'),
    path('api/v1/asambleistas/actualizar/<int:pk>', views.ListAsambleistasView.as_view({'patch': 'partial_update'}), name='actualiza_asambleista'),
    path('api/v1/asambleistas/eliminar/<int:pk>', views.ListAsambleistasView.as_view({'post': 'destroy'}), name='elimina_asambleista'),    
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/asambleistas/self', views.UsuarioView.as_view({'get': 'list'}), name='get_self_user'),
    path('api/v1/asambleistas/apoderados', views.ApoderadosView.as_view({'get': 'list'}), name='get_apoderados')
]