from django.db import models
from startup.models import ProductService, Member
from transactions.models import Transaction
import random
import string
# Create your models here.


def generate_random_id():
    characters = string.ascii_letters + string.digits  # Using letters and digits for the id
    random_id = ''.join(random.choice(characters) for _ in range(9))
    while random_id == Cart.objects.filter(cart_id=random_id)[0]:
        random_id = ''.join(random.choice(characters) for _ in range(9))
    return random_id


class CartItem(models.Model):
    product = models.ForeignKey(ProductService, on_delete=models.SET_NULL)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    cart_id = models.CharField(max_length=9, default=generate_random_id, unique=True)
    items = models.ManyToManyField(CartItem)
    client = models.ForeignKey(Member, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart_id
    

class Purchase(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL)
    payment = models.OneToOneField(Transaction, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=(
        ('PENDING', 'PENDING'),
        ('ACCEPTED', 'ACCEPTED'),
        ('FAILED', 'FAILED'),
    ))


