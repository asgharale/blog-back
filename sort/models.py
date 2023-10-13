from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=25)
    link = models.SlugField(max_length=25)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(unique=True, max_length=25)
    link = models.SlugField(max_length=25)

    def __str__(self):
        return self.name
