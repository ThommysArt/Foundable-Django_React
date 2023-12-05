from rest_framework import generics, viewsets
from .serializers import *

class FreelanceSkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = FreelanceSkill.objects.all()
    serializer_class = FreelanceSkillSerializer

class FreelanceSkillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FreelanceSkill.objects.all()
    serializer_class = FreelanceSkillSerializer

class FreelancerViewSet(viewsets.ModelViewSet):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer

class FreelanceServiceImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = FreelanceServiceImage.objects.all()
    serializer_class = FreelanceServiceImageSerializer

class FreelanceServiceImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FreelanceServiceImage.objects.all()
    serializer_class = FreelanceServiceImageSerializer

class FreelanceServiceViewSet(viewsets.ModelViewSet):
    queryset = FreelanceService.objects.all()
    serializer_class = FreelanceServiceSerializer

class FreelaceServiceOfferViewSet(viewsets.ModelViewSet):
    queryset = FreelanceServiceOffer.objects.all()
    serializer_class = FreelanceServiceOfferSerializer