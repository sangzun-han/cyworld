from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CyUser(AbstractUser):
    email = models.EmailField(max_length=50)
    sex = models.CharField(max_length = 10, null = True)
    birth = models.DateField(null = True)
    title = models.TextField(null = True)
    today = models.IntegerField(null = True)
    total = models.IntegerField(null = True)
    profile_img = models.ImageField(null = True, upload_to="%Y/%m/%d")
    today_f = models.DateField(null = True)
    full_name = models.CharField(max_length = 30, null = True)
    contents = models.TextField(null = True)

    def __str__(self):
        return self.full_name