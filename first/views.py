# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

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
                    return HttpResponse('Connecté.')
                else:
                    return HttpResponse('Utilisateur desactivé')
            else:
                return HttpResponse('utilisateur invalide')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form':form})

def user_logout(request):
    return HttpResponse('Logout')

def home(request):
    return render(request, 'pages/home.html')
