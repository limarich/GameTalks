from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Post, Thread, Comment, Tag
from categories.models import Forum, Category
from profiles.models import Profile
from django.shortcuts import render, redirect
from django.db.models import Count
import json

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


    return render(request, 'pages/explore.html', {'forums_and_threads': forums_and_threads})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, thread_id=thread_id)
    posts = Post.objects.filter(thread=thread)
    
    posts_with_details = []
    for post in posts:
        comments_count = Comment.objects.filter(post=post).count()
        
        post_details = {
            'post': post,
            'comments_count': comments_count,
            'tags': post.tags.all(),
        }
        posts_with_details.append(post_details)
    
    return render(request, 'pages/thread_detail.html', {'thread': thread, 'posts_with_details': posts_with_details})

@login_required
def post(request,post_id):
    post = get_object_or_404(Post, post_id=post_id)
    comments = Comment.objects.filter(post=post)
    tags = post.tags.all()
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



@login_required
def create_post(request):
    print('ramonnn')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        description = request.POST.get('description')
        tags = json.loads(request.POST.get('tags'))
        thread_id = request.POST.get('thread_id')
        
        if title and content:
            new_post = Post.objects.create(
                title=title,
                content=content,
                user=request.user ,
                thread_id= thread_id 
            )
            
            if tags:
                for tag_id in tags:
                    tag = Tag.objects.get(tag_id=tag_id)
                    new_post.tags.add(tag)
            
            
            return JsonResponse({'post_id': str(new_post.post_id)})

    threads = Thread.objects.all()
    forums = Forum.objects.all()
    categories = Category.objects.all()
  
  
    return render(request, 'pages/create-post.html', {'threads': threads, 'forums': forums, 'categories': categories})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        description = request.POST.get('description')
        tags = request.POST.get('tags')
        
        if tags:
            tags = json.loads(tags)
        else:
            tags = [] 

        thread_id = request.POST.get('thread_id')
        
        if title and content:
            # Atualiza os campos do post existente
            post.title = title
            post.content = content
            post.thread_id = thread_id
            post.save()
            
            if tags:
                for tag_id in tags:
                    tag = Tag.objects.get(tag_id=tag_id)
                    post.tags.add(tag)  
            
            return JsonResponse({'post_id': str(post.post_id)})

    threads = Thread.objects.all()
    forums = Forum.objects.all()
    categories = Category.objects.all()
    
    tags = post.tags.all()

    return render(request, 'pages/edit-post.html', {'post': post, 'threads': threads, 'forums': forums, 'categories': categories, 'tags': tags })

@login_required
def tag_list(request):
    tags = Tag.objects.all().values('tag_id', 'title')  
    
    tags_list = list(tags) 
    
    return JsonResponse({'tags': tags_list})

@login_required
def create_tag(request):
    if request.method == 'POST':
        tag_title = request.POST.get('tag_title')
        
        if tag_title:
            try:
                tag, created = Tag.objects.get_or_create(title=tag_title)
                if created:
                    return JsonResponse({'tag_id': tag.tag_id, 'tag_title': tag.title})
                else:
                    return JsonResponse({'message': 'Tag already exists'})
            except Exception as e:
                return JsonResponse({'message': str(e)})
    
    return render(request, 'pages/create-tag.html')

@login_required
def thread_list(request):
    threads = Thread.objects.all()
    forum = Forum.objects.all()
    return render(request, 'threads_list.html', {'threads': threads})

@login_required
def forum_list(request):
    forum = Forum.objects.all()
    forum_data = list(forum.values())  
    return JsonResponse(forum_data, safe=False)

@login_required
def create_thread(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        forum_id = request.POST.get('forum_id')  


        forum = Forum.objects.get(id=forum_id) 

        thread = Thread.objects.create(title=title, slug=slug, forum=forum)

        response_data = {
            'id': thread.thread_id,
            'title': thread.title,
            'slug': thread.slug,
        }
        return JsonResponse(response_data)
        
    return render(request, 'pages/create-thread.html')

@login_required
def create_forum(request):
    if request.method == 'POST':
        title = request.POST.get('forum_title')
        slug = request.POST.get('forum_description')
        category_id = request.POST.get('category_id')  
        
        if title and category_id: 
            try:
                forum, created = Forum.objects.get_or_create(title=title, slug=slug)
                forum.categories.add(category_id)
                if created:
                    return JsonResponse({'forum_id': forum.id, 'forum_title': forum.title})
                return JsonResponse({'message': 'Forum already exists'})
            except ValueError as e:
                return JsonResponse({'message': str(e)})
    
    return render(request, 'pages/create-tag.html')