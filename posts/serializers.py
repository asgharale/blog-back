from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'description', 'meta_des', 'thumbnail', 'body', 'category', 'tags', 'create_date', 'update', 'read_time', 'views', 'likes', 'author', 'coms')


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'description', 'thumbnail', 'category', 'create_date', 'read_time', 'views', 'likes', 'author')