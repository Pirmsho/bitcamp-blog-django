from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


def home(request):
    return render(request, 'home.html')


def posts(request):
    list = ['post_1', 'post_2', 'post_3', 'post_4']
    return render(request, 'blog/post_list.html', {'list':list})