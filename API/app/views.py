from django.shortcuts import render
from .serializers import UserSerializer, CancionSerializer
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import cancion
# Create your views here.



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class CancionViewSet(viewsets.ModelViewSet):
    queryset = cancion.objects.all()
    serializer_class = CancionSerializer
