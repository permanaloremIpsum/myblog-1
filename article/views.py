# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def myview(request):
    return HttpResponse('<h1>this is my view</h1>')


def hello_world(request):
    return HttpResponse('Hello World')


def nama_saya(request, nama, umur):
    return HttpResponse('Hello nama saya adalah {}, umur saya adalah {} tahun'.format(nama, umur))


def home(request):
    return render(request, 'index.html')