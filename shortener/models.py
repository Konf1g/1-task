from django.db import models
from django.contrib.auth.models import User


class Urls(models.Model):
    originalUrl = models.CharField(max_length=5000)
    auto_increment_id = models.AutoField(primary_key=True)
