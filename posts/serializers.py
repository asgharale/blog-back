from rest_framework import serializers
from posts.models import Post
from sort.serializers import CategorySerializer, TagSerializer


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'description', 'meta_des', 'thumbnail_url', 'body', 'category', 'tags', 'create_date', 'update', 'read_time', 'views', 'likes', 'author', 'coms')

    def get_thumbnail_url(self, post):
        request = self.context.get('request')
        thumbnail_url = post.thumbnail.url
        return request.build_absolute_uri(thumbnail_url)


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'description', 'thumbnail', 'category', 'create_date', 'read_time', 'views', 'likes', 'author')