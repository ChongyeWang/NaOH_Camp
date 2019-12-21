from django.contrib import admin
from face.models import Face


class FaceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Face, FaceAdmin)

