# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from article.models import Category, Post
from article.forms import RegistrationUserForm


# Create your views here.
def myview(request):
    return HttpResponse('<h1>this is my view</h1>')


def hello_world(request):
    return HttpResponse('Hello World')


def nama_saya(request, nama, umur):
    return HttpResponse('Hello nama saya adalah {}, umur saya adalah {} tahun'.format(nama, umur))


def category(request):
    return HttpResponse('halaman list category')


def home(request):
    categories = Category.objects.all()
    list_post = Post.objects.all().order_by('created_on')[:3]
    anu = {
        'categories': categories,
        'postingan': list_post,
        'nama': 'Ayip',
    }
    return render(request, 'home.html', anu)

@login_required(login_url='/login/')
def post_detail(request, slug):
    data = {
        'categories': Category.objects.all(),
        'post': Post.objects.get(slug=slug),
    }
    return render(request, 'detail.html', data)


def loginview(request):
    if request.user.is_authenticated():
        return redirect('/')

    data = {}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('/dashboard/')
        else:
            messages.warning(
                request, 'Gagal. Silahkan cek user dan password anda')

    return render(request, 'login.html', data)


def logoutview(request):
    logout(request)
    return redirect('/')


def registrationview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # form.save()
            print form.cleaned_data.get('username')
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationUserForm()
    data = {'form':form}
    return render(request, 'registration.html', data)

def dashboard(request):
    return render(request, 'dashboard.html')