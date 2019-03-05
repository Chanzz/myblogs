from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User

'''
class BlogUsers(models.Model):
    nickname = models.CharField(max_length=20)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    registertime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nickname
'''


class ArticlePost(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    createdtime = models.DateTimeField(default=timezone.now)
    updatedtime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-createdtime',)

    def __str__(self):
        return self.title
