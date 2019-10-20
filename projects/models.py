from django.db import models

# Create your models here.
class Personal_info(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 0)


