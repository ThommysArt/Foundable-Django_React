from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Member(AbstractUser):
    email = models.EmailField(max_length=256)
    image = models.ImageField(upload_to='images/member')
    countryCode = models.IntegerField(default=237, max_length=3)
    phoneNumber = models.IntegerField(default=000000000, max_length=9)
    address = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    

