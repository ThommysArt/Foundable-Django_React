from rest_framework import serializers
from .models import *
from membership.serializers import MemberSerializer


class FreelanceSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelanceSkill
        fields = '__all__'


class FreelancerSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    skills = FreelanceSkillSerializer(many=True, read_only=True)

    class Meta:
        model = Freelancer
        fields = '__all__'


class FreelanceServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelanceServiceImage
        fields = '__all__'


class FreelanceServiceSerializer(serializers.ModelSerializer):
    skills = FreelanceSkillSerializer(many=True)
    images = FreelanceServiceImageSerializer(many=True)
    freelancer = FreelancerSerializer()

    class Meta:
        model = FreelanceService
        fields = '__all__'


class FreelanceServiceOfferSerializer(serializers.ModelSerializer):
    freelancer = FreelancerSerializer()
    client = MemberSerializer()
    service = FreelanceServiceSerializer()

    class Meta:
        model = FreelanceServiceOffer
        fields = '__all__'