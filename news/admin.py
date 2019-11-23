from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)

