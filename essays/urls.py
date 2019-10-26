from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.essays, name="post_essay"),
    path("view/", views.view_essays, name="view_essays"),
    path("<int:pk>/", views.essay_details, name="essay_details"),
    
] 