from django.urls import path
from posts.views import posts_list

urlpatterns = [
    path('v1/posts/', posts_list),
]