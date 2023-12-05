

from django.db import models
from . import CURRENCY_CHOICES
import string, random

def generate_random_id():
    characters = string.ascii_uppercase + string.digits
    length = 9  # Using letters and digits for the id
    while True:
        random_id = ''.join(random.choice(characters) for _ in range(length))
        if not Transaction.objects.filter(t_id=random_id).exists():
            break
    return random_id



class Transaction(models.Model):
    t_id = models.CharField(max_length=9, default=generate_random_id())
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")
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
