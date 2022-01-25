from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, get_list_or_404
from . models import *
from django.db import models
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, ListView)
from django.urls import reverse_lazy, reverse
from .models import Post
from .forms import CommetModelForm
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator


class PostListView(ListView):
    paginate_by = 3
    model = Post


# class PostDetailView(DetailView):
#     form_class = CommentForm
#     success_url = '/thanks/'
#     model = Post


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


# def posts(request):
#     post_list = Post.objects.all()

#     paginator = Paginator(post_list, 3) # Show 25 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {'posts':posts, 'form':com_form, 'page_obj':page_obj }
#     return render(request, 'blog/post_list.html', context)


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommetModelForm()
    if request.method == 'POST':
        form = CommetModelForm(request.POST)
        print(request.user)
        print(form.fields)
        print('post')
        if form.is_valid():
            print(form.cleaned_data)
            form.cleaned_data['post'] = post
            form.cleaned_data['author'] = request.user
            print(form.cleaned_data)
            form.save()
            return home(request)
    return render(request, 'blog/post_detail.html', {'post': post, 'com_form':form})

# აქედან იქნება Comment

# აქედან იქნება Comment# -----------------------------------------------


# def comment_create(request):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             text = request.POST['comment_text']
#             return HttpResponseRedirect('blog:post')
#     else:
#         form = CommentForm()
#     return render(request, 'post', {'form': form})



class CommentCreateView(CreateView):
    fields = '__all__'
    model = Comment


def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'blog/comment_detail.html', {'comment': comment})


def comment_list(request):
    comments = get_list_or_404(Comment)
    # return HttpResponse('This is comment list')
    context = {'posts': posts}
    return render(request, 'blog/comment_list.html', {'comments': comments})


# -----------------------------------------------
# აქედან იქნება Category

class CategoryListView(ListView):
    paginate_by = 3
    model = Category


class CategoryDetailView(DetailView):
    model = Category

