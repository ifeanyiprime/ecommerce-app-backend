from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    profile_img = models.ImageField(upload_to="profiles", null=True, blank=True)

