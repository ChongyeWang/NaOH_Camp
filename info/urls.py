from django.urls import path
from . import views

urlpatterns = [
    path("", views.info_index, name="info_index"),
    path("author/", views.author_index, name="author_index"),
    path("team/", views.info_team, name="info_team")
]