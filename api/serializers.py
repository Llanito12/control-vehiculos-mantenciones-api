from rest_framework import serializers
from .models import Vehiculo, Mantencion

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class MantencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantencion
        fields = '__all__'