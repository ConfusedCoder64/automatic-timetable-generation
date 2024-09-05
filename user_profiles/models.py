from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ImageField, ValidationError
from .manager import UserManager
import os

# Create your models here.
class Notification(models.Model):
    sender = models.TextField(max_length=100, default='')
    receiver = models.TextField(max_length=100, default='')
    notification = models.TextField(max_length=200)
    approved = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    acknowledged = models.BooleanField(default=False)

class CustomUserModel(AbstractUser):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1].lower()

        if ext not in ["jpg", "png", "gif", "jpeg"]:
            raise ValidationError(f"invalid image extension: {filename}")

        if instance.username:
            filename = f"{instance.username}.{ext}"
        else:
            filename = f"{filename}.{ext}"
        return os.path.join("profile pictures/", filename)
    contact_no = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    address = models.TextField(max_length=200,default = '')
    stream = models.TextField(max_length=15)
    days_present = models.IntegerField(null=True)
    profile_picture = models.ImageField(upload_to=wrapper)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()


