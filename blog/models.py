from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(default='', max_length=50)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.title


