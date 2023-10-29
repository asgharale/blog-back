from rest_framework.response import Response
from rest_framework.views import APIView
from posts.serializers import PostSerializer, PostListSerializer
from posts.models import Post
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class PostList(APIView):
    def get(self, request, fromat=None):
        posts = Post.objects.filter(publish=True)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)



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

        serializer = PostSerializer(post)
        return Response(serializer.data)



class PostsSearchView(APIView):
    def post(self, request, fromat=None):
        data = request.data["s"]
        posts = Post.objects.filter(title__contains=data)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)




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




class CatView(APIView):
    def get_objs(self, cat):
        try:
            return Post.objects.filter(category__link=cat, publish=True)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, cat, fromat=None):
        posts = self.get_objs(cat)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class TagView(APIView):
    def get_objs(self, tag):
        try:
            return Post.objects.filter(tags__link=tag, publish=True)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, tag, fromat=None):
        posts = self.get_objs(tag)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)