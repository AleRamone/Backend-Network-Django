from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def feed(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente')
            return redirect('feed')

    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'social/register.html', context)

def profile(request):
    return render(request, 'social/profile.html')
