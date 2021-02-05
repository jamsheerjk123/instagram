from django.urls import path
from posts import views

urlpatterns=[
    path("", views.home_view, name="home"),
    path("add/", views.add_post, name="add_post")
]