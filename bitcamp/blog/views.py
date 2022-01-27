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
from django.db.models import Q

class PostListView(ListView):
    paginate_by = 3
    model = Post

def posts(request):
    phrase_q = Q()
    q = request.GET.get('phrase')
    if q:
        phrase_q &= (Q(text__icontains=q) | Q(description__icontains=q) | Q(title__icontains=q))
    post_list = Post.objects.filter(phrase_q).order_by('-pk')
    paginator = Paginator(post_list, 3)  # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/post_list.html', context)



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
    one_post_from_category = PostModel.objects.all()[0:3]
    return render(request, 'home.html', {'posts':one_post_from_category})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommetModelForm()

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

