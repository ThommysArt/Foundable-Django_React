from rest_framework import serializers
from .models import *
from startup.serializers import ProductServiceSerializer, MemberSerializer
from transactions.serializers import TransactionSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductServiceSerializer

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    client = MemberSerializer

    class Meta:
        model = Cart
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    cart = CartSerializer
    payment = TransactionSerializer

    class Meta:
        model = Purchase
        fields = '__all__'