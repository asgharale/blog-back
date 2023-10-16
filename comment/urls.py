from django.urls import path
from comment.views import PostCommentList


urlpatterns = [
    path("v1/comments/<int:pk>", PostCommentList.as_view()),
]