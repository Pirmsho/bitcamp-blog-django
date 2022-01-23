from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, get_list_or_404
from . models import *
from django.db import models
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, ListView)
from django.urls import reverse_lazy, reverse
from .models import Post
from .forms import *
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


class PostListView(ListView):
    paginate_by = 6
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    fields = '__all__'
    model = Post


class PostUpdateView(UpdateView):
    fields = '__all__'
    # fields = ('username', 'first_name', 'last_name', 'image')
    model = Post


# ეს არ შლის სურათს მედია ფაილიდან. გადასაწყვეტია ...
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')


def home(request):
    return render(request, 'home.html')


def posts(request):
    posts = get_list_or_404(Post)
    # context = {'posts':posts}
    return render(request, 'blog/post_list.html', {'posts': posts})


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post)
    return render(request, 'blog/post_detail.html', {'post': post})


def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'blog/comment_detail.html', {'comment': comment})


def comment_list(request):
    comments = get_list_or_404(Comment)
    # return HttpResponse('This is comment list')
    context = {'posts': posts}
    return render(request, 'blog/comment_list.html', {'comments': comments})
