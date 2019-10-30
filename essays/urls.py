from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.essays, name="post_essay"),
    path("view/", views.view_essays, name="view_essays"),
    path("<int:pk>/", views.essay_details, name="essay_details"),

    path("<int:pk>/rate/1", views.one_star, name="one_star"),
    path("<int:pk>/rate/2", views.two_star, name="two_star"),
    path("<int:pk>/rate/3", views.three_star, name="three_star"),
    path("<int:pk>/rate/4", views.four_star, name="four_star"),
    path("<int:pk>/rate/5", views.five_star, name="five_star"),
    
] 