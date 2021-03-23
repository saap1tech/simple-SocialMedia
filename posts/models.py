from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    user = models.CharField(max_length=30)
    image = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Like(models.Model):
    user = models.CharField(max_length=30)
    post = models.CharField(max_length=30)

    def __str__(self):
        return self.user

class Comment(models.Model):
    user = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    comment = models.TextField()

    def __str__(self):
        return self.user