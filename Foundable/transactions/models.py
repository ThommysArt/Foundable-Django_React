

from django.db import models
from subscriptions.models import currency_choices
import string, random

def generate_random_id():
    characters = string.ascii_uppercase + string.digits  # Using letters and digits for the id
    random_id = ''.join(random.choice(characters) for _ in range(9))
    while random_id == Transaction.objects.filter(t_id=random_id)[0]:
        random_id = ''.join(random.choice(characters) for _ in range(9))
    return random_id


class Transaction(models.Model):
    t_id = models.CharField(max_length=9, default=generate_random_id())
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=currency_choices, default="USD")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(
        ('PENDING', 'PENDING'),
        ('ACCEPTED', 'ACCEPTED'),
        ('FAILED', 'FAILED'),
    ))
    details = models.JSONField()
    invoice_number = models.CharField(max_length=255)
    notify_url = models.CharField(max_length=255)
    return_url = models.CharField(max_length=255)
    cancel_return_url = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment: {self.t_id} {self.currency}"
