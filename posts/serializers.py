from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'description', 'meta_des', 'thumbnail', 'body', 'category', 'tags', 'create_date', 'update', 'read_time', 'publish', 'views', 'likes', 'author')