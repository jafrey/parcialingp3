from django.shortcuts import render
from .serializers import UserSerializer, CancionSerializer
from rest_framework import routers, serializers, viewsets, generics, filters
from django.contrib.auth.models import User
from .models import cancion
# Create your views here.

from django.views.decorators.csrf import csrf_exempt


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class CancionViewSet(viewsets.ModelViewSet):
    queryset = cancion.objects.all()
    serializer_class = CancionSerializer


class ObtenerUsuario(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


#Estos dos campos me permiten filtrar por username y saber si existe en el login

    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)

#

#    def get_queryset(self):
#        """
#        This view should return a list of all the purchases for
#        the user as determined by the username portion of the URL.
#        """
#        username = self.kwargs['username']
#
#        return User.objects.filter(username=username)
