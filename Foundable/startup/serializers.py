from rest_framework import serializers
from .models import *
from membership.serializers import MemberSerializer

class EntrepreneurSerializer(serializers.ModelSerializer):
    member = MemberSerializer()

    class Meta:
        model = Entrepreneur
        fields = ['id', 'fullName', 'member', 'bio']


class ProductServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductService
        fields = ['id', 'name', 'description', 'quantity', 'price', 'available']

class ProductServiceImageSerializer(serializers.ModelSerializer):
    productService = ProductServiceSerializer
    class Meta:
        model = ProductServiceImage
        fields = ['id', 'productService', 'image']


class StartupSerializer(serializers.ModelSerializer):
    entrepreneur = EntrepreneurSerializer()
    product_services = ProductServiceSerializer(many=True)

    class Meta:
        model = Startup
        fields = ['id', 'entrepreneur', 'product_services', 'name', 'email']


class FinancialRecordSerializer(serializers.ModelSerializer):
    startup = StartupSerializer()

    class Meta:
        model = FinancialRecord
        fields = ['id', 'startup', 'month', 'profit', 'expenses']


class EmployeeSerializer(serializers.ModelSerializer):
    startup = StartupSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'startup', 'name', 'member', 'salary']


class EmployeeProfitSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = EmployeeProfit
        fields = ['id', 'employee', 'month', 'profit']


class JobPostSerializer(serializers.ModelSerializer):
    startup = StartupSerializer()

    class Meta:
        model = JobPost
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    job = JobPostSerializer()
    member = MemberSerializer()

    class Meta:
        model = JobApplication
        fields = '__all__'
