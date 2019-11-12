from django.shortcuts import render, render_to_response

#importa el hasher de passwords de django
from django.contrib.auth.hashers import make_password

#para que no joda la seguridad
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#Imports para usar json y urllib
import json
import urllib
import requests



@csrf_exempt
def login(request):

    if request.method == "GET":

    	return render_to_response('login.html')

    else:

     usuario = request.POST['usuario']
     contra = request.POST['contrasenia']
     contra = make_password(contra)


     url = 'http://api:8001/ousuario/?search=' + usuario

     response = requests.get(url)
     jsonData = json.loads(response.text)

     if jsonData == '[]':

            return render_to_response('login.html')

     else:

         jsonData = json.loads(data)


     if usuario == jsonData[username] and contra == jsonData[password]:

                return render_to_response('principal.html')
