from django.contrib import admin
from ranking.models import Rating


class RatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rating, RatingAdmin)
