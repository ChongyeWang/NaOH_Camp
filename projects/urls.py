from django.urls import path

from . import views


urlpatterns = [
	path("", views.home, name="home"),
	path("map", views.map, name="map"),
    path("resource", views.project_index, name="project_index"),
    path("setting/", views.setting, name="setting"),
    path("resource/background", views.background, name="background"),
    path("resource/setting", views.game_setting, name="game_setting"),
    path("resource/download", views.download, name="download"),
    path("resource/mod", views.mod, name="mod"),
]
