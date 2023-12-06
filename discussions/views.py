from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post, Thread, Comment, Tag
from profiles.models import Profile
from django.shortcuts import render, redirect
from django.db.models import Count
from datetime import datetime

def teste(request):
    return HttpResponse("ok")

@login_required
def posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)
    else:
        posts = []
    return HttpResponse(posts)

def homepage(request):
    return render(request, 'pages/homepage.html')

@login_required
def explore(request):
    threads_with_most_posts = Thread.objects.annotate(num_posts=Count('post')).order_by('-num_posts')

    forums_and_threads = {}
    for thread in threads_with_most_posts:
        forum_title = thread.forum.title

        if forum_title not in forums_and_threads:
            forums_and_threads[forum_title] = []

        forums_and_threads[forum_title].append({'thread': thread, 'posts_count': thread.num_posts})

    print(forums_and_threads)

    return render(request, 'pages/explore.html', {'forums_and_threads': forums_and_threads})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, thread_id=thread_id)
    posts = Post.objects.filter(thread=thread)
    
    posts_with_details = []
    for post in posts:
        comments_count = Comment.objects.filter(post=post).count()
        tags = Tag.objects.filter(post=post)
        
        post_details = {
            'post': post,
            'comments_count': comments_count,
            'tags': tags,
        }
        posts_with_details.append(post_details)
    
    return render(request, 'pages/thread_detail.html', {'thread': thread, 'posts_with_details': posts_with_details})

@login_required
def post(request,post_id):
    post = get_object_or_404(Post, post_id=post_id)
    comments = Comment.objects.filter(post=post)
    tags = Tag.objects.filter(post=post)
    post.created_at = post.created_at.strftime("%d/%m/%Y")
    profile = Profile.objects.filter(user=request.user).first()
    
    return render(request, 'pages/post.html', {'post': post, 'comments': comments, 'tags': tags, 'profile': profile})

@login_required
def add_comment_to_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        
        comment_content = request.POST.get('comment_content')
        if comment_content:
            comment = Comment.objects.create(
                content=comment_content,
                user=request.user,
                post=post
            )
            return redirect('discussions:post', post_id=post_id)
    
    return HttpResponse("Erro ao adicionar comentário.")