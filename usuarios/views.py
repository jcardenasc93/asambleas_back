from django.shortcuts import render
from .models import Asambleista
# Create your views here.


def createUser(request):
    asambleista = Asambleista(username='asambleista_test', first_name='Don asambleista Test',
                              email='asambleista@asambleista.com', inmueble='INT10 AP 301', documento='1032555678')
    asambleista.set_password('asambleas2020')
    asambleista.save()
