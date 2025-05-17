from rest_framework import serializers
from .models import Service
from mechanics.serializers import MechanicSerializer


class ServiceSerializer(serializers.ModelSerializer):
    mechanic = MechanicSerializer(read_only=True)
    class Meta:
        model = Service
        fields = ['id', 'mechanic', 'name', 'price', 'duration']
        read_only_fields = ['id', 'mechanic']
