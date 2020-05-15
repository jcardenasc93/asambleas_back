from django.shortcuts import render
from .models import Asambleista
# Create your views here.


def createUser(request):
    asambleista = Asambleista(username='asambleista', password='asambleista', first_name='Don asambleista',
                              email='asambleista@asambleista.com', inmueble='INT9 AP 301', documento='1032555678')
    asambleista.save()
