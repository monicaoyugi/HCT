from django.test import TestCase
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response

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
