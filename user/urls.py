from django.urls import path
from .views import UserRegister, UserLogin, UserLogout, UsersView, UserProfile



urlpatterns = [
    path('v1/register', UserRegister.as_view()),
    path('v1/Login', UserLogin.as_view()),
    path('v1/logout', UserLogout.as_view()),
    path('v1/profiles', UsersView.as_view()),
    path('v1/profiles/<slug:username>', UserProfile.as_view())
]