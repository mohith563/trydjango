from django.db import models

# Create your models here.

class Article(models.Model):
    title       = models.CharField(max_length=20)
    article     = models.TextField(blank=True, null=True)
    author      = models.TextField(blank=False,null=False)
