from django.urls import path
from . import views

urlpatterns = [
    path("", views.ranking, name="ranking"),
    path("<int:pk>/", views.ranking_details, name="rating_details"),
    path("create/", views.post_ranking, name="post_ranking"),

    path("<int:pk>/rate/1", views.one_star, name="r_one_star"),
    path("<int:pk>/rate/2", views.two_star, name="r_two_star"),
    path("<int:pk>/rate/3", views.three_star, name="r_three_star"),
    path("<int:pk>/rate/4", views.four_star, name="r_four_star"),
    path("<int:pk>/rate/5", views.five_star, name="r_five_star"),
    
] 