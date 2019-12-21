from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.face_upload, name="face_upload"),
    
] 