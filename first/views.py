# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
                else:
                    message = 'Utilisateur desactivé'
                    return render(request, 'pages/login.html', {'form':form,'msg':message})
            else:
                message = 'utilisateur invalide'
                return render(request, 'pages/login.html', {'form':form,'msg':message})
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return render(request, 'pages/logged_out.html')

@login_required
def home(request):
    return render(request, 'pages/home.html')

@login_required
def quality(request):
    return render(request, 'pages/quality.html')

@login_required
def alignment(request):
    if request.method == 'POST':
        return render(request, 'pages/alignement.html',{"result":request.POST.get('test')})
    else:
        return render(request, 'pages/alignement.html')

@login_required
def var_calling(request):
    return render(request, 'pages/var_calling.html')

@login_required
def annotation(request):
    return render(request, 'pages/annotation.html')
