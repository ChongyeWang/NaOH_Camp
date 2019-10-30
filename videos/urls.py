from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.videos, name="post_video"),
    path("view/", views.view_videos, name="view_videos")
    
] 