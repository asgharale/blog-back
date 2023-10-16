from rest_framework.response import Response
from rest_framework.views import APIView
from comment.serializers import CommentSerializer
from comment.models import Comment
from django.http import Http404


class PostCommentList(APIView):
    def get_objs(self, pk):
        try:
            return Comment.objects.all().filter(post=pk, confirm=True)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, fromat=None):
        comments = self.get_objs(pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)