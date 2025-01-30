from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

# @login_required
def posts_list(request):
    posts = Post.objects.filter(status='published')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/list.html', {'page_obj': page_obj})

@login_required
def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        if request.user == post.author:
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_details', post_id=post.id)
        else:
            return redirect('post_details', post_id=post.id)
    else:
        form = PostForm(instance=post) if request.user == post.author else None
    return render(request, 'posts/details.html', {'form': form, 'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'posts/form_details.html', {'form': form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.user != post.author:
        return redirect('post_details', post_id=post.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_details', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/form_details.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.user == post.author:
        post.delete()
    return redirect('posts_list')