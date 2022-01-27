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


# @@@@@@@@@@@@@@@@@ დეკორატორი ჭირდება რომ მხოლოდ ადმინმა შეძლოს მენტორის დარეგისტრირება
def register(request):
    registered = False
    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = AuthorForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)
        # Check to see both forms are valid
        if user_form.is_valid():
            # Save User Form to Database
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            # Now we deal with the extra info!
            # Can't commit yet because we still need to manipulate
            # profile = profile_form.save(commit=False)
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            # profile.user = user
            # Check if they provided a profile picture
            if 'image' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                user.image = request.FILES['image']
            # Now save model
            user.save()
            # Registration Successful!
            registered = True
            return HttpResponseRedirect(reverse('user:login'))
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = AuthorForm()
        # profile_form = UserProfileInfoForm()
    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'user/author_form.html',
                          {'form':user_form,
                        #    'profile_form':profile_form,
                           'registered':registered})



def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
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