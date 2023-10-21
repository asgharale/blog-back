from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('An Email Address is Required.')
        if not username:
            raise ValueError('An Userame is Required.')
        if not password:
            raise ValueError('A Password is Required.')


        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username,  password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user



class MyUser(AbstractBaseUser, PermissionsMixin):
    # Auth data
    email = models.EmailField(unique=True, max_length=150, verbose_name="Email Address")
    username = models.CharField(unique=True, max_length=50)


    # Personal Detail (for staff users)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True, verbose_name='biography')
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

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(blank=True, null=True)
    last_login = models.DateField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username',]
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return (self.is_active and self.is_staff)
    def has_perms(perm_list, obj=None):
        return (self.is_active and self.is_staff)
    def has_module_perms(self, package_name):
        return (self.is_active and self.is_staff and self.is_admin)

    def __str__(self):
        return self.email    
    def get_full_name(self):
        return f"{self.name} {self.last_name}"
    
    def get_short_name(self):
        return self.first_name
