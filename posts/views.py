from rest_framework.response import Response
from rest_framework.views import APIView
from posts.serializers import PostSerializer
from posts.models import Post
from django.http import Http404


class PostList(APIView):
    def get(self, request, fromat=None):
        posts = Post.objects.filter(publish=True)
        serializer = PostSerializer(posts, many=True)
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




class PostLikeView(APIView):
    pass



class CatView(APIView):
    def get_objs(self, cat):
        try:
            return Post.objects.filter(category__link=cat, publish=True)
        except Post.DoesNotExist:
            raise Http404
        
        
    def get(self, request, cat, fromat=None):
        posts = self.get_objs(cat)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class TagView(APIView):
    def get_objs(self, tag):
        try:
            return Post.objects.filter(tags__link=tag, publish=True)
        except Post.DoesNotExist:
            raise Http404
        
        
    def get(self, request, tag, fromat=None):
        posts = self.get_objs(tag)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)