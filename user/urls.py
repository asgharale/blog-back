from django.urls import path
from .views import UserRegister, UserLogin, UserLogout



urlpatterns = [
    path('v1/register', UserRegister.as_view()),
    path('v1/Login', UserLogin.as_view()),
    path('v1/logout', UserLogout.as_view()),
]