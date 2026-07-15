from rest_framework import serializers
from .models import Campaña, Actividad

class CampañaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaña
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'