from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Transpose


# class ActiveUserManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)
# Create your models here.
class CustomUser(AbstractUser):
   email=models.EmailField(unique=True)
   objects = CustomUserManager()
   @classmethod
   def get_all_users(cls):
        return cls.objects.all()
   @classmethod
   def get_active_users(cls):
       return cls.objects.filter(is_active=True)
   USERNAME_FIELD='email'
   REQUIRED_FIELDS=[]
   def __str__(self):
        return self.email


class Base(models.Model):
    create = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Modified", auto_now=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        abstract: bool = True


# class Profile(Base):
