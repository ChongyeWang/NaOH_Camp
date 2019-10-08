from django.urls import path

from . import views


urlpatterns = [
	path("", views.home, name="home"),
    path("resource/", views.project_index, name="project_index"),
    path("setting/", views.setting, name="setting"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]