from django.db import models
from membership.models import Member
# Create your models here.

    
class FreelanceSkill(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='skills_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Freelancer(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1500)
    skills = models.ManyToManyField(FreelanceSkill)
    experience = models.TextField(max_length=1500)
    education = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name
    

class FreelanceServiceImage(models.Model):
    image = models.ImageField(upload_to='services/images')

    def __str__(self):
        return self.image.name
    

class FreelanceService(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    skill = models.ManyToManyField(FreelanceSkill)
    images = models.ManyToManyField(FreelanceServiceImage)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FreelanceServiceOffer(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    client = models.ForeignKey(Member, on_delete=models.CASCADE)
    service = models.ForeignKey(FreelanceService, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='accepted', choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.freelancer.display_name} - {self.service.title}"


