from rest_framework import serializers
from reviews.models import Review
from rest_framework import serializers
from .models import Review
from users.models import User  # lub użyj get_user_model()

class ReviewSerializerMechanic(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)
    # mechanic_name = serializers.CharField(source='mechanic.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Review
        read_only_fields = ('id', 'user', 'service', 'created_at', 'updated_at')
        fields = ('id', 'note', 'content', 'created_at', 'updated_at', 'user', 'service', 'service_name', 'user_email')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        read_only_fields = ('id', 'user', 'service', 'created_at', 'updated_at')
        fields = ('id', 'note', 'content', 'created_at', 'updated_at', 'user', 'service')

class ReviewCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # tylko te dwa pola klient może wysłać
        fields = ('note', 'content')\


