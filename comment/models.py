from django.db import models
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    # admin deside
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.post.title}"

