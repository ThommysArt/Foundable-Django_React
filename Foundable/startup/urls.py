
from django.urls import path
from .views import *


urlpatterns = [
    path('entrepreneur/', EntrepreneurListCreateAPIView.as_view()),
    path('entrepreneur/<int:pk>/', EntrepreneurRetrieveUpdateDestroyAPIView.as_view()),
    path('product-service/', ProductServiceListCreateAPIView.as_view()),
    path('product-service/<int:pk>/', ProductServiceRetrieveUpdateDestroyAPIView.as_view()),
    path('product-service-image/', ProductServiceImageListCreateAPIView.as_view()),
    path('product-service-image/<int:pk>/', ProductServiceImageRetrieveUpdateDestroyAPIView.as_view()),
    path('startup/', StartupListCreateAPIView.as_view()),
    path('startup/<int:pk>/', StartupRetrieveUpdateDestroyAPIView.as_view()),
    path('financial-record/', FinancialRecordListCreateAPIView.as_view()),
    path('financial-record/<int:pk>/', FinancialRecordRetrieveUpdateDestroyAPIView.as_view()),
    path('employee/', EmployeeListCreateAPIView.as_view()),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path('employee-profit/', EmployeeProfitListCreateAPIView.as_view()),
    path('employee-profit/<int:pk>/', EmployeeProfitRetrieveUpdateDestroyAPIView.as_view()),
    path('job-post/', JobPostListCreateAPIView.as_view()),
    path('job-post/<int:pk>/', JobPostRetrieveUpdateDestroyAPIView.as_view()),
    path('job-application/', JobApplicationListCreateAPIView.as_view()),
    path('job-application/<int:pk>/', JobApplicationRetrieveUpdateDestroyAPIView.as_view()),
]
