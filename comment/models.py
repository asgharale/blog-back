from django.db import models
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    com = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    # admin deside
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.post
