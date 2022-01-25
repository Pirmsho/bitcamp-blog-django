from django.shortcuts import redirect, render
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


class PostCreateView(CreateView):
    fields = '__all__'
    model = Post


class PostUpdateView(UpdateView):
    fields = '__all__'
    model = Post


# ეს არ შლის სურათს მედია ფაილიდან. გადასაწყვეტია ...
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')


def home(request):
    return render(request, 'home.html')


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommetModelForm()
    print(type(request.user))

    if request.method == 'POST':
        form = CommetModelForm(request.POST)
        if form.is_valid():
            form.instance.post = post
            id = request.POST['id']
            form.instance.author = Author.objects.get(pk=id)
            form.save()
            return redirect(reverse("blog:posts"))
    return render(request, 'blog/post_detail.html', {'post': post, 'com_form':form})


# -----------------------------------------------
# აქედან იქნება Category

class CategoryListView(ListView):
    paginate_by = 3
    model = Category


class CategoryDetailView(DetailView):
    model = Category

