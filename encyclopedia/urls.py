from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lol", views.index, name="new_page")
]
