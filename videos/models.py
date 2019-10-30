from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import os
from django.core.exceptions import ValidationError

class Post(models.Model):
    user = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    body = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

def get_video_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "videos/%s-%s" % (slug, filename)  

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.avi', '.flv', '.mkv', '.rm', '.wmv', '.mov']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


class Videos(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    video = models.FileField(upload_to=get_video_filename,
                              verbose_name='video',
                              validators=[validate_file_extension])