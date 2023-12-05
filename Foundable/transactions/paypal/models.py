from django.db import models
import string, random
from .. import CURRENCY_CHOICES

def generate_random_id():
    characters = string.ascii_uppercase + string.digits
    length = 9  # Using letters and digits for the id
    while True:
        random_id = ''.join(random.choice(characters) for _ in range(length))
        if not PaypalPayment.objects.filter(t_id=random_id).exists():
            break
    return random_id


class PaypalPayment(models.Model):
    payment_id = models.CharField(max_length=9, default=generate_random_id(), unique=True)
    transaction_details = models.JSONField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")
    date = models.DateTimeField(auto_now_add=True)
    return_url = models.TextField()
    cancel_url = models.TextField()