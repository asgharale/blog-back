from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Post(models.Model):
    STATUSES = [('pub', 'publish'), ('drf', 'draft')]

    title = models.CharField(max_length=255, unique=True)
    link = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=350)
    meta_des = models.CharField(max_length=150, blank=True)
    thumbnail = models.ImageField(upload_to='thumbs/%Y-%m')

    # REACH TEXT EDITOR
    body = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(default=timezone.now)
    read_time = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=3, choices=STATUSES, default='pub')
    views = models.PositiveIntegerField(editable=False, default=3)

    author = models.ForeignKey(User, default='admin', on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.link