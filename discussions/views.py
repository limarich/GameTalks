from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post, Thread
from django.shortcuts import render, redirect
from django.db.models import Count

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
    
    threads_and_posts = {}
    for thread in threads_with_most_posts:
        posts = Post.objects.filter(thread=thread)
        threads_and_posts[thread] = list(posts)
    
    return render(request, 'pages/explore.html', {'threads_and_posts': threads_and_posts})