from django.contrib.auth import get_user_model, login, logout, authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework import permissions, status
from .models import User, Profile
from django.http import Http404
from .models import User
from .validations import email_validation, user_validation


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def create(self, clean_data):
        user = User.objects.create(
            email=clean_data['email'],
            username=clean_data['username'],
            password=clean_data['password'])
        user.first_name = clean_data['first_name']
        user.last_name = clean_data['last_name']
        
        return user


    def post(self, request):
        clean_data = request.data
        if email_validation(clean_data['email']):
            serializer = UserRegisterSerializer(data=clean_data)
            if serializer.is_valid(raise_exception=True):
                user = self.create(clean_data)
                if user:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Reaponse(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)


    def post(self, request):
        clean_data = request.data

        assert email_validation(clean_data['email'])
        # assert validate_pass(data['password'])

        serializer = UserLoginSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = user_validation(clean_data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)



class UserProfile(APIView):
    def get_obj(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

        try:
            prof = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise Http404

        # return how to combine to model instance in django

    def get(self, request, username, fromat=None):
        user = self.get_obj(username)
        



class UserLogout(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
