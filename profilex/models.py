from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField('NAME', max_length=200)
    text = models.TextField('Strong Point', blank=True)

    thumbnail = models.ImageField(
        'Thumbnails', upload_to='thumbnails/', null=True, blank=True)
    upload = models.FileField(
        'Video', upload_to='uploads/%Y/%m/%d/', null=True)

    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    updated_date = models.DateTimeField('Updated Date', auto_now=True)

    def __str__(self):
        return self.title
