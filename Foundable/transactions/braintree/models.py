from django.db import models
import string, random
from .. import CURRENCY_CHOICES

def generate_random_id():
    characters = string.ascii_uppercase + string.digits  # Using letters and digits for the id
    random_id = ''.join(random.choice(characters) for _ in range(9))
    while random_id == BraintreePayment.objects.filter(t_id=random_id)[0]:
        random_id = ''.join(random.choice(characters) for _ in range(9))
    return random_id


class BraintreePayment(models.Model):
    payment_id = models.CharField(max_length=9, default=generate_random_id(), unique=True)
    transaction_details = models.JSONField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")
    date = models.DateTimeField(auto_now_add=True)