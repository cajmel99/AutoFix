from rest_framework import serializers
from .models import Mechanic
from users.serializers import UserSerializer


class MechanicSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Mechanic
        fields = ['id', 'user', 'name', 'address', 'description', 'contact_phone', 'city', 'rating', 'created_at']
        read_only_fields = ['id', 'user', 'rating', 'created_at']
