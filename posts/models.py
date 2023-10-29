from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from sort.models import Category, Tag
from ckeditor.fields import RichTextField



User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    link = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=350)
    meta_des = models.CharField(max_length=150, blank=True)
    thumbnail = models.ImageField(upload_to='thumbs/%Y-%m')

    # CKEDITOR FIELD
    body = RichTextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags =models.ManyToManyField(Tag, related_name='posts', null=True, blank=True)

    create_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(default=timezone.now)
    read_time = models.PositiveSmallIntegerField()
    publish = models.BooleanField(default=True)
    views = models.PositiveIntegerField(editable=False, default=3)
    liked_users = models.ManyToManyField(User, blank=True, related_name="likes")

    author = models.ForeignKey(User, default='admin', on_delete=models.SET_DEFAULT, related_name='posts')

    @property
    def coms(self):
        return self.comments.count()

    @property
    def likes(self):
        return self.liked_users.count()

    def __str__(self):
        return f"{self.link} -- {self.title}"
    

    class Meta:
        ordering = ["-create_date", "-update"]