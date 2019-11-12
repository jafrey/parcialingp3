#Importa las bases de la tabla que crea django para los usuarios
from django.contrib.auth.models import User

#importa estas 3 herramientas para usar de rest_framework
from rest_framework import routers, serializers, viewsets

#importa los modelos
from .models import cancion

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password']

# Serializers define the API representation.
class CancionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cancion
        fields = ['nom_cancion', 'desc_cancion', 'anio_salida']
