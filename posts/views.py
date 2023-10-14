from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.serializers import PostSerializer
from posts.models import Post

@api_view(['GET',])
def posts_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)