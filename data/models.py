from django.db import models

# Create your models here.


class Content(models.Model):
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.TextField()
