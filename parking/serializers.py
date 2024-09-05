from rest_framework import serializers
from .models import Commercial_Establishment, Vehicle


class CommercialEstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commercial_Establishment
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
