
from django.urls import path
from .views import *


urlpatterns = [
    path('transaction/', TransactionViewSet.as_view),
    path('paypal-payment/', PayPalPaymentAPIView.as_view()),
    path('paypal-retrieve/', RetrievePaypalPaymentAPIView.as_view()),
    path('paypal-list/', ListPaypalPaymentAPIView.as_view()),
    path('stripe-payment/', StripePaymentAPIView.as_view()),
    path('stripe-list/', ListStripePaymentAPIView.as_view()),
    path('stripe-retrieve/', RetrieveStripePaymentAPIView.as_view()),
    path('braintree-payment/', BraintreePaymentAPIView.as_view()),
    path('braintree-list/', ListBraintreePaymentAPIView.as_view()),
    path('braintree-retrieve/', RetrieveBraintreePaymentAPIView.as_view()),
]
