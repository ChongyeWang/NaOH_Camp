from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    
    name = models.CharField(max_length=15)
    link = models.CharField(max_length=200)