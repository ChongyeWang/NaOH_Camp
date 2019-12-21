from django.urls import path
from . import views

urlpatterns = [
    path("", views.face_auth_create, name="face_auth_create")
] 