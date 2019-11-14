from django.shortcuts import render, render_to_response

#importa el hasher de passwords de django
from django.contrib.auth.hashers import make_password

#para que no joda la seguridad
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


#Imports para usar json y urllib
import json
import requests


@csrf_exempt
def MostrarLogin(request):

    if request.method == "GET":

    	return render_to_response('login.html')

    else:

     usuario = request.POST['usuario']
     contra = request.POST['contrasenia']


    # result = requests.post('http://api:8000/ousuario/?username=' + usuario + '&'+)

    r = requests.post("http://api:8000/login", data={'username': usuario, 'password': contra})
    print(r.status_code, r.reason)







    # return render_to_response('principal.html', { 'usuario' : result.text })
