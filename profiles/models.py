from django.db import models
from django.contrib.auth.models import AbstractUser
import django_filters
# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=288)
    last_name = models.CharField(max_length=233)
    profile_picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default_image/default_profile_image.png')

    def __str__(self) -> str:
        return self.first_name
