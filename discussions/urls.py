from django.urls import path
from . import views

app_name = "discussions"

urlpatterns = [
    path('teste', views.teste, name="teste"),
    path('posts', views.posts, name="posts"),
    path('explore', views.explore, name="explore"),
    path('post/<uuid:post_id>/', views.post, name="post"),
    path('post/add_comment/', views.add_comment_to_post, name="add_comment_to_post"),
    path('', views.homepage, name="homepage"),
    
]
