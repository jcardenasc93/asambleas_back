from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [    
    path('api/v1/new_asam/', views.createUser),
    path('api/v1/auth/', include('djoser.urls.authtoken'))
]