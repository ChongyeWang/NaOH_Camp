from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Rating(models.Model):
    
    name = models.CharField(max_length=10)
    body = models.CharField(max_length=2000, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    rate = models.FloatField(default=0)
    rate_total = models.FloatField(default=0)
    rate_num = models.IntegerField(default=0)


class Comment(models.Model):
    author = models.CharField(max_length=20, default='')
    body = models.TextField(max_length=200, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE)