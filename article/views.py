# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from article.models import Category, Post


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
    return render(request, 'index.html', anu)


def post_detail(request, slug):
    data = {
        'categories': Category.objects.all(),
        'post': Post.objects.get(slug=slug),
    }
    return render(request, 'detail.html', data)
