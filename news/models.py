from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
