from django.urls import path
from . import views

app_name = "discussions"

urlpatterns = [
    path('teste', views.teste, name="teste"),
    path('posts', views.posts, name="posts")
]
