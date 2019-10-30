from django.contrib import admin
from videos.models import Post, Videos


class PostAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Videos, VideoAdmin)
