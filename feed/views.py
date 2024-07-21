from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm


def home_view(request):
    objects = Post.objects.all().order_by('-created_at')
    context = {'objects': objects}
    return render(request, 'home.html', context)


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home_view')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'post.html', context)


@login_required
def profile_view(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'profile.html', context)


def open_view(request, id):
    info = get_object_or_404(Post, id=id)
    context = {'info': info}
    return render(request, 'edit_delete.html', context)


def delete_picture(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    if request.method == "POST":
        post.delete()
        return redirect('profile_view')
    return render(request, 'delete.html', context)


def update_desc(request, id):
    update = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=update)
    if form.is_valid():
        form.save()
        return redirect('profile_view')
    context = {'form': form}
    return render(request, 'update.html', context)


def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'comment.html', context)
