from django.urls import path
from comment.views import PostCommentList


urlpatterns = [
    path("v1/comments/<slug:link>", PostCommentList.as_view()),
]