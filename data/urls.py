from django.urls import path
from . import views

urlpatterns = [
    path("analyze/", views.data_analyze, name="data_analyze"),
    path("predict/", views.data_predict, name="data_predict"),
]