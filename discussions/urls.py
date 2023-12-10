from django.urls import path
from . import views

app_name = "discussions"

urlpatterns = [
    path('teste', views.teste, name="teste"),
    path('posts', views.posts, name="posts"),
    path('explore', views.explore, name="explore"),
    path('thread/<uuid:thread_id>/', views.thread_detail, name="thread_detail"),
    path('post/<uuid:post_id>/', views.post, name="post"),
    path('post/add_comment/', views.add_comment_to_post, name="add_comment_to_post"),
    path('post/create_post/', views.create_post, name="create_post"),
    path('thread/create_thread', views.create_thread, name="create_thread"),
    path('tags', views.tag_list, name="tags_list"),
    path('post/create_post/new_tag', views.create_tag, name="create_tag"),
    path('post/create_post/create_thread', views.create_thread, name="create_thread"),
    path('', views.homepage, name="homepage"),
    
]
