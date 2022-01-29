import re
from django.db import models
from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DeleteView, DetailView, ListView)
from django.urls import reverse_lazy, reverse
from .models import Author
from .forms import *
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


def home(request):
    return render(request, 'home.html')


class AutorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class CreateAuthorView(CreateView):
    fields = ('username', 'first_name', 'last_name', 'image', 'password')
    model = Author


class UpdateAuthorView(UpdateView):
    fields = ('username', 'first_name', 'last_name', 'image')
    model = Author


# ეს არ შლის სურათს მედია ფაილიდან. გადასაწყვეტია ...
class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('user:authors')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = AuthorForm(data=request.POST)
        print(user_form)
        if user_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password1)
            user.save()
            if 'image' in request.FILES:
                user.image = request.FILES['image']
            user.save()
            # Registration Successful!
            registered = True
            return HttpResponseRedirect(reverse('user:login'))
        else:
            print(user_form.errors)
    else:
        user_form = AuthorForm()
    return render(request,'user/author_form.html',
                          {'form':user_form,
                           'registered':registered})



def my_login(request):
    if request.method == 'POST':
        print(request.user)
        print(request.POST)
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('blog:home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        #Nothing has been provided for username or password.
        return render(request, 'user/login.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))