from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="chat_index"),
    path("all_users/", views.all_users, name="all_users"),
    path('<str:room_name>/', views.room, name='room')
] 