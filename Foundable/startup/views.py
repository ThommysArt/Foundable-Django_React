from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
# Create your views here.

# Entrepreneur views
class EntrepreneurListCreateAPIView(ListCreateAPIView):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer
    
class EntrepreneurRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer


# ProductService view
class ProductServiceListCreateAPIView(ListCreateAPIView):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer

class ProductServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer


# ProductServiceImage view
class ProductServiceImageListCreateAPIView(ListCreateAPIView):
    queryset = ProductServiceImage.objects.all()
    serializer_class = ProductServiceImageSerializer

class ProductServiceImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductServiceImage.objects.all()
    serializer_class = ProductServiceImageSerializer


# Startup view
class StartupListCreateAPIView(ListCreateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

class StartupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


# FinancialRecord view
class FinancialRecordListCreateAPIView(ListCreateAPIView):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer

class FinancialRecordRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer


# Employee view
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# EmployeeProfit view
class EmployeeProfitListCreateAPIView(ListCreateAPIView):
    queryset = EmployeeProfit.objects.all()
    serializer_class = EmployeeProfitSerializer

class EmployeeProfitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeProfit.objects.all()
    serializer_class = EmployeeProfitSerializer


class JobPostListCreateAPIView(ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class JobApplicationListCreateAPIView(ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobApplicationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    
