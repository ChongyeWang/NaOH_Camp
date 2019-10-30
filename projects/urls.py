from django.urls import path

from . import views


urlpatterns = [
	path("", views.home, name="home"),
	path("map", views.map, name="map"),
    path("resource", views.project_index, name="project_index"),
    path("setting/", views.setting, name="setting"),
    path("setting/my_post", views.my_post, name="my_post"),
    path("setting/my_video", views.my_video, name="my_video"),
    path("setting/my_column", views.my_column, name="my_column"),
    path("resource/background", views.background, name="background"),
    path("resource/setting", views.game_setting, name="game_setting"),
    path("resource/download", views.download, name="download"),
    path("resource/mod", views.mod, name="mod"),
    path("resource/history", views.history, name="history")
]
