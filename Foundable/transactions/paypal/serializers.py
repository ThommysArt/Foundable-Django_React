from rest_framework import serializers
from .models import *

class PaypalPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaypalPayment
        fields = "__all__"