from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SignUpForm, LogInForm, PostForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .models import Post, User
from django.views.generic import UpdateView

# Create your views here.

def feed(request):
    model = Post
    posts = Post.objects.filter(author=request.user).order_by()
    return render(request,'feed.html', {'posts':posts})

def edit_feed(request, post_id):
    post = Post.objects.get(pk = post_id)
    update_post = Post.objects.filter(pk = post_id)
    form = PostForm(request.POST)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            update_post.update(text = form.cleaned_data.get('text'))
            return(redirect('feed'))
    return(render(request, 'edit_feed.html', {'form': form, 'user': post}))


def show_user(request, user_id):
    users = get_user_model().objects.get(pk = user_id)
    posts = Post.objects.filter(author_id = user_id).order_by()
    return(render(request, 'show_user.html', {'user':users}))

def make_new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posts = Post.objects.all().filter(author = request.user)
            user = form.save(request.user)
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'make_new_post.html',{"form": form})


def user_list(request):
    model = User
    posts = User.objects.all()
    return render(request, 'user_list.html', {'users': posts  })


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def home(request):
    return render(request,'home.html')

def log_out(request):
    logout(request)
    return redirect('home')
