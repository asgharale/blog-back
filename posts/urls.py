from django.urls import path
from posts.views import PostList, PostDetail, CatView, TagView

urlpatterns = [
    path('v1/posts/', PostList.as_view()),
    path('v1/post/<slug:link>', PostDetail.as_view()),
    path('v1/cpost/<slug:cat>', CatView.as_view()),
    path('v1/tpost/<slug:tag>', TagView.as_view()),
]