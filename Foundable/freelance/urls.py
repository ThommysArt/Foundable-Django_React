
from django.urls import path
from .views import *


urlpatterns = [
    path('freelance-skill', FreelanceSkillListCreateAPIView.as_view()),
    path('freelance-skill/<int:pk>/', FreelanceSkillRetrieveUpdateDestroyAPIView.as_view()),
    path('freelancer', FreelancerViewSet.as_view),
    path('freelance-service', FreelanceServiceViewSet.as_view),
    path('freelance-service-image', FreelanceServiceImageListCreateAPIView.as_view()),
    path('freelance-service-image/<int:pk>/', FreelanceServiceImageRetrieveUpdateDestroyAPIView.as_view()),
    path('freelance-service-offer', FreelaceServiceOfferViewSet.as_view),
]
