from django.urls import path
from posts.views import PostList, PostDetail

urlpatterns = [
    path('v1/posts/', PostList.as_view()),
    path('v1/post/<slug:link>', PostDetail.as_view()),
]