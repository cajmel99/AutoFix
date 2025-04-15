from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'mechanic', 'name', 'price', 'duration']
        read_only_fields = ['id', 'mechanic']
