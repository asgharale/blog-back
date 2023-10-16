from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from sort.models import Category, Tag




class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    link = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=350)
    meta_des = models.CharField(max_length=150, blank=True)
    thumbnail = models.ImageField(upload_to='thumbs/%Y-%m')

    # REACH TEXT EDITOR
    body = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags =models.ManyToManyField(Tag, related_name='posts')

    create_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(default=timezone.now)
    read_time = models.PositiveSmallIntegerField()
    publish = models.BooleanField(default=True)
    views = models.PositiveIntegerField(editable=False, default=3)
    likes = models.PositiveIntegerField(default=0)

    author = models.ForeignKey(User, default='admin', on_delete=models.SET_DEFAULT, related_name='posts')

    def coms(self):
        return self.comments.count()

    def __str__(self):
        return f"{self.link} -- {self.title}"
    

    class Meta:
        ordering = ["-create_date", "-update"]
    
    # comments