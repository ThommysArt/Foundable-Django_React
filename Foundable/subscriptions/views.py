from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SubscriptionService, Subscription, StartupSubscription, FreelancerSubscription
from .serializers import SubscriptionServiceSerializer, SubscriptionSerializer, StartupSubscriptionSerializer, FreelancerSubscriptionSerializer

class SubscriptionServiceListCreateView(generics.ListCreateAPIView):
    queryset = SubscriptionService.objects.all()
    serializer_class = SubscriptionServiceSerializer

class SubscriptionServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionService.objects.all()
    serializer_class = SubscriptionServiceSerializer

class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class StartupSubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = StartupSubscription.objects.all()
    serializer_class = StartupSubscriptionSerializer

class StartupSubscriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StartupSubscription.objects.all()
    serializer_class = StartupSubscriptionSerializer

class FreelancerSubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = FreelancerSubscription.objects.all()
    serializer_class = FreelancerSubscriptionSerializer

class FreelancerSubscriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FreelancerSubscription.objects.all()
    serializer_class = FreelancerSubscriptionSerializer
