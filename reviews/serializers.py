from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    # amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Review
        fields = '__all__'
