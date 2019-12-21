from django.contrib import admin
from ranking.models import Rating, Comment


class RatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rating, RatingAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)