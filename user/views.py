from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from .models import User, Profile
from django.http import Http404


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        # VALIDATION REQUIRED
        # clean_data = MyValidation(request.data)
        clean_data = request.data
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Reaponse(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data

        # assert validate_email(data.email)
        # assert validate_pass(data.password)

        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.chek_user(data)
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



class UsersView(APIView):
    pass