from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title       = models.CharField(max_length=20)
    article     = models.TextField(blank=True, null=True)
    author      = models.CharField(blank=False,null=False, max_length=40)

    def get_absolute_url(self):
        return reverse('articles:article-detail',kwargs={'id':self.id})

