from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from posts.serializers import PostSerializer, PostListSerializer
from posts.models import Post
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.pagination import PageNumberPagination



class PostList(ListAPIView):
    queryset = Post.objects.filter(publish=True)
    serializer_class = PostListSerializer



class PostDetail(APIView):
    def get_obj(self, link):
        try:
            return Post.objects.get(link=link, publish=True)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, link, fromat=None):
        post = self.get_obj(link)

        # viewer adding
        post.views += 1
        post.save()

        serializer = PostSerializer(post, context= {"request": request})
        return Response(data=serializer.data)



class PostsSearchView(ListAPIView):
    serializer_class = PostListSerializer
    def get_queryset(self):
        queryset = Post.objects.filter(title__contains=self.kwargs['s'], publish=True)
        return queryset




class PostLikeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_obj(self, pk):
        try:
            return Post.objects.get(pk=pk, publish=True)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_obj(pk)
        if not request.user in post.liked_users.all():
            post.liked_users.add(request.user)
            post.save()
        return Response(status=status.HTTP_200_OK)




class CatView(ListAPIView):
    serializer_class = PostListSerializer
    def get_queryset(self):
        try:
            return Post.objects.filter(publish=True, category__link=self.kwargs['cat'])
        except Post.DoesNotExist:
            raise Http404


class TagView(ListAPIView):
    serializer_class = PostListSerializer
    def get_queryset(self):
        try:
            return Post.objects.filter(publish=True, tags__link=self.kwargs['tag'])
        except Post.DoesNotExist:
            raise Http404
            