from rest_framework import serializers
from .models import *
from startup.serializers import StartupSerializer
from freelance.serializers import FreelancerSerializer


class SubscriptionServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionService
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    subscription = SubscriptionServiceSerializer()
    class Meta:
        model = Subscription
        fields = '__all__'


class StartupSubscriptionSerializer(serializers.ModelSerializer):
    startup = StartupSerializer()
    subscription = SubscriptionServiceSerializer()
    class Meta:
        model = StartupSubscription
        fields = '__all__'


class FreelancerSubscriptionSerializer(serializers.ModelSerializer):
    subscription = SubscriptionServiceSerializer()
    freelancer = FreelancerSerializer()
    class Meta:
        model = FreelancerSubscription
        fields = '__all__'