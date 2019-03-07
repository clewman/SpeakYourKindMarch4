from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def index(request):
    #print(request.user.username)
    return render(request, 'users/index.html', {})


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('game:game'))

    # return HttpResponseRedirect(reverse('users:index'))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('game:game'))
    return HttpResponseRedirect(reverse('users:register'))


def register(request):
    return render(request, 'users/register.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'users/register.html', {})
