from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm


def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instace = form.save(commit=False)
            instace.author = request.user
            instace.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()
    ctx = {
        "posts": posts,
        'form': form
    }
    return render(request, "blog/index.html", ctx)


def LogoPage(request):
    return render(request, 'blog/loginPage.html')


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html')