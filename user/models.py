from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email Address", max_length=150)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff and instance.is_active:
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Personal Detail (for staff users)
    bio = models.TextField(blank=True, verbose_name='biography')
    # PHONE_NUMBER
    # phone_num
    date_birth = models.DateField(blank=True, null=True)
    pub_email = models.EmailField(blank=True, max_length=150)
    insta_id = models.SlugField(blank=True, max_length=50, verbose_name="Instagram ID")
    tel_id = models.SlugField(blank=True, max_length=50, verbose_name="Telegram ID")
    etaa_id = models.SlugField(blank=True, max_length=50, verbose_name="Etaa ID")
    what_id = models.SlugField(blank=True, max_length=50, verbose_name="Whatsapp ID")
    twitt_id = models.SlugField(blank=True, max_length=50, verbose_name="Twitt ID")
    Youtube_id = models.SlugField(blank=True, max_length=50, verbose_name="Youtube ID")
    ###


    def __str__(self):
        return self.user
    
    class Meta:
        ordering = ('id',)