from django.urls import path
from .views import *


urlpatterns = [
    path('subscription-service/', SubscriptionServiceListCreateView.as_view()),
    path('subscription-service/<int:pk>/', SubscriptionServiceRetrieveUpdateDestroyView.as_view()),
    path('subscription/', SubscriptionListCreateView.as_view()),
    path('subscription/<int:pk>/', SubscriptionRetrieveUpdateDestroyView.as_view()),
    path('startup-subscription/', StartupSubscriptionListCreateView.as_view()),
    path('startup-subscription/<int:pk>/', StartupSubscriptionRetrieveUpdateDestroyView.as_view()),
    path('freelancer-subscription/', FreelancerSubscriptionListCreateView.as_view()),
    path('freelancer-subscription/<int:pk>/', FreelancerSubscriptionRetrieveUpdateDestroyView.as_view()),
]
