from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

# .은 현재 디렉토리 or 애플리케이션을 의미한다.
# 동일한 디렉토리이기 때문에 .py 를 붙이지 않아도 된다.
from .models import Post
from .forms import PostForm

def index(request):
    return HttpResponse("You're looking blog.")


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def base(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/base.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('blog:post_edit', args=(post.pk,)))
            # return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    # return HttpResponseRedirect(reverse('blog:post_new.html', args=(form,)))


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return HttpResponseRedirect(reverse('blog:post_detail', args=(pk,)))

    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


