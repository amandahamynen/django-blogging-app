from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    path("all/", views.blogpost_list_all, name="blogpost_list_all"),
    path("my/", views.blogpost_list_my, name="blogpost_list_my"),
    path("<int:blogpost_id>/", views.blogpost_detail, name="blogpost_detail"),
    path("<int:blogpost_id>/edit/", views.blogpost_edit, name="blogpost_edit"),
    path("create_blogpost/", views.blogpost_create, name="blogpost_create"),
    path("<int:blogpost_id>/toggle_privacy/", views.blogpost_toggle_privacy, name="blogpost_toggle_privacy"),
    path("<int:blogpost_id>/delete/", views.blogpost_delete, name="blogpost_delete"),
]