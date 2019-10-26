from django.contrib import admin
from essays.models import Post, Images


class PostAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Images, ImageAdmin)
