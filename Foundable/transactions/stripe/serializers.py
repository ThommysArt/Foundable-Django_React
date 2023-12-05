
from .models import StripePayment
from rest_framework import serializers

class StripePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripePayment
        fields = ('payment_id', 'transaction_details', 'amount', 'currency', 'date','return_url', 'cancel_url')