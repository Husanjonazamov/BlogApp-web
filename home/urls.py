from django.urls import path

from .views import *

urlpatterns = [
    path("blog/", index, name="blog-index"),
    path("post_detail/<int:pk>/", post_detail, name='blog-post-detail'),
]
