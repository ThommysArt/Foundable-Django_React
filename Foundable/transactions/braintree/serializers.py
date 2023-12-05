from rest_framework import serializers
from .models import BraintreePayment


class BraintreePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BraintreePayment
        fields = "__all__"
