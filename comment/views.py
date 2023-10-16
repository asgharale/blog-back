from rest_framework.response import Response
from rest_framework.views import APIView
from comment.serializers import CommentSerializer
from comment.models import Comment
from django.http import Http404


class PostCommentList(APIView):
    def get_objs(self, link):
        try:
            return Comment.objects.filter(post__link=link, confirm=True)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, link, fromat=None):
        comments = self.get_objs(link)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)