from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_links, name="get_all_links"),
    path("upload/", views.upload_link, name="upload_link")
] 