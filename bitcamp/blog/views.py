from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from django.shortcuts import get_object_or_404, get_list_or_404
from . models import *


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
