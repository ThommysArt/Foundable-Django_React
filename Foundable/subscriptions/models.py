
from django.db import models
from startup.models import Startup
from freelance.models import Freelancer
from . import CURRENCY_CHOICES



class SubscriptionService(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=(
        ('sales', 'Sales'),
        ('advertisement', 'Advertisement'),
        ('organisation', 'Organisation'),
        ('hiring', 'Hiring'),
        ('employments', 'Employments'),
        ('marketing', 'Marketing'),
        ('collaboration', 'Collaboration'),
        ('management', 'Management'),
    ))
    description = models.TextField()
    charges_per_month = models.DecimalField(max_digits=12, decimal_places=2)
    charges_per_year = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')


class Subscription(models.Model):
    subscription = models.ForeignKey(SubscriptionService, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=(
        ('subscribed', 'Subscribed'),
        ('unsubscribed', 'Unsubscribed'),
        ('canceled', 'Canceled'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)


class StartupSubscription(Subscription):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)


class FreelancerSubscription(Subscription):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    




