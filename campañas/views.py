from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Campaña, Actividad
from .serializers import CampañaSerializer, ActividadSerializer

class CampañaViewSet(viewsets.ModelViewSet):
    queryset = Campaña.objects.all()
    serializer_class = CampañaSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer