from rest_framework import serializers
from reviews.models import Review


from rest_framework import serializers
from .models import Review
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


