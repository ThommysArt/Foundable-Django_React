
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import member
from . import serializers
from rest_framework.permissions import IsAuthenticated
from .serializers import *



class SignUpView(generics.CreateAPIView):
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.object = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(generics.CreateAPIView):
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            member = serializer.validated_data['member']

            if member.check_password(serializer.data['password']):
                request._member = member
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response({'password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ForgotPasswordView(generics.CreateAPIView):
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            member = serializer.validated_data['member']

            # Send email with reset password link

            return Response({'email': ['Email sent.']}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateAccountView(generics.UpdateAPIView):
    serializer_class = MemberSerializer
    model = member
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.member



class DeleteAccountView(generics.DestroyAPIView):
    model = member
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.member
