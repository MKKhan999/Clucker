from django.shortcuts import render, redirect
from .forms import SignUpForm, LogInForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .models import Post

# Create your views here.

def feed(request):
    model = Post
    posts = Post.objects.filter(created_at__isnull=False).order_by()
    return render(request,'feed.html', {'posts':posts})

def user_list(request):
    model = get_user_model()
    users = get_user_model().objects.all()
    return render(request, 'user_list.html', {'users': users})

def show_user(request):
    pass
    # users = get_user_model().objects.get(id=user_id)
    # posts = Post.objects.filter(author_id = user_id).order_by()

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
