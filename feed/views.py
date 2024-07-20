from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home_view(request):
    objects = Post.objects.all()
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

