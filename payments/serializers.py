from rest_framework import serializers
from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'status', 'created_at', 'payment_method']