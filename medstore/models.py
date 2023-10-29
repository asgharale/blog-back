from django.db import models



class Image(models.Model):
    image = models.ImageField(upload_to="image/%Y-%m")
    alt = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    
    @property
    def get_image_url(self):
        return self.image.url
    
    def __str__(self):
        return f"{self.name} - {self.get_image_url}"


class Video(models.Model):
    video = models.FileField(upload_to="video/%Y-%m")
    alt = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)

    @property
    def get_video_url(self):
        return self.video.url

    def __str__(self):
        return f"{self.name} - {self.get_video_url}"

class File(models.Model):
    fiel = models.FileField(upload_to="file/%Y-%m")
    name = models.CharField(max_length=255, unique=True)

    @property
    def get_file_url(self):
        return self.file.url

    def __str__(self):
        return f"{self.name} - {self.get_file_url}"

