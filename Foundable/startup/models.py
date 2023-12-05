from django.db import models
from membership.models import Member



class Entrepreneur(models.Model):
    fullName = models.CharField(max_length=100)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL)
    bio = models.TextField()
    # Add other relevant fields like contact information, social media links, etc.
    
    def __str__(self):
        return self.name


class ProductService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12)
    available = models.BooleanField(default=True)
    # Add any other relevant fields like price, availability, etc.
    
    def __str__(self):
        return self.name
    

class ProductServiceImage(models.Model):
    productService = models.ForeignKey(ProductService, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images')
    
    def __str__(self):
        return self.image.name


class Startup(models.Model):
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    product_services = models.ManyToManyField(ProductService)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    # Add other relevant fields for the startup
    
    def __str__(self):
        return self.name


class FinancialRecord(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    month = models.DateField()
    profit = models.DecimalField(max_digits=12, decimal_places=2)
    expenses = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"{self.startup.name} - {self.month}"
    

class Employee(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.name


class EmployeeProfit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    profit = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"{self.employee.name} - {self.month}"
    

class JobPost(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=(
        ('active', 'Active'),
        ('taken', 'Taken'),
        ('canceled', 'Canceled'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class JobApplication(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ))




