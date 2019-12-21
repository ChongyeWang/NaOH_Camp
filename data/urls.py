from django.urls import path
from . import views

urlpatterns = [
    path("predict/", views.data_predict, name="data_predict"),
]