from django.urls import path
from sort.views import TPostList, CPostList, TagList, CategoryList

urlpatterns = [
    path("v1/tposts/<int:pk>", TPostList.as_view()),
    path("v1/cposts/<int:pk>", CPostList.as_view()),
    path("v1/tags", TagList.as_view()),
    path("v1/cats", CategoryList.as_view()),
]