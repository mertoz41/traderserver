from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_new_user", views.create_new_user, name="create_new_user"),
]