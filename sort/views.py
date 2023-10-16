from rest_framework.response import Response
from rest_framework.views import APIView
from sort.models import Category, Tag
from sort.serializers import CategorySerializer, TagSerializer


class CategoryList(APIView):
    def get(self, request, fromat=None):
        cats = Category.objects.all()
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)

class TagList(APIView):
    def get(self, request, fromat=None):
        cats = Tag.objects.all()
        serializer = TagSerializer(cats, many=True)
        return Response(serializer.data)
    
