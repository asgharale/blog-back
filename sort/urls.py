from django.urls import path
from sort.views import TagList, CategoryList

urlpatterns = [
    path("v1/tags", TagList.as_view()),
    path("v1/cats", CategoryList.as_view()),
]