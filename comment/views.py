from rest_framework.response import Response
from rest_framework.views import APIView
from comment.serializers import CommentSerializer
from comment.models import Comment
from django.http import Http404
from rest_framework.generics import ListAPIView


class PostCommentList(ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.filter(post__link=self.kwargs['link'], confirm=True)