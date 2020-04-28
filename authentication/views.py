from django.test import TestCase
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.response import Response
from .models import Profile
from rest_framework.permissions import IsAuthenticated
# Create your tests here.


class RegistrationAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.user
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


class ProfileAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        print(Profile.objects.filter(user=1).first().user.email)
        return Profile.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        print(request.user)
        serializer = ProfileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)
