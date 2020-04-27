from django.test import TestCase
from rest_framework import status
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer, ProfileCreateSerializer
from rest_framework.response import Response
from .models import Profile
# Create your tests here.


class RegistrationAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        response = {
            'data': {
                'user': user_data,
                'message': 'user created sucesfully'
            }
        }
        return Response(response)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.data

        response = {
            'data': {
                'user': dict(user),
                'message': 'you have succesfully loged in'
            }
        }

        return Response(response)


class ProfileCreateAPIView(GenericAPIView):
    model = Profile
    serializer_class = ProfileCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(Profile.objects.filter(user=1).first().user.username)
        serializer = ProfileCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)
