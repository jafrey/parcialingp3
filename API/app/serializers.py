from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import cancion

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# Serializers define the API representation.
class CancionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cancion
        fields = ['nom_cancion', 'desc_cancion', 'anio_salida']
