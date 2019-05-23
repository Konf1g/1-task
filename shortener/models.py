from django.db import models
from django.contrib.auth.models import User


class Urls(models.Model):
    originalUrl = models.CharField(max_length=5000)
    newUrl = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(null=True)
    auto_increment_id = models.AutoField(primary_key=True)
