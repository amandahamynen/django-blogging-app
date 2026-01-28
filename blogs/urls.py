from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.blogpost_list, name="blogpost_list"),
    path("<int:blogpost_id>/", views.blogpost_detail, name="blogpost_detail"),
    path("create_blogpost/", views.blogpost_create, name="blogpost_create"),
]