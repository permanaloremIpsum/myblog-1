# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = "Category"
        ordering = ['name']
 
    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=255, null=True)
    category = models.ForeignKey(Category,related_name='post_category', null=True)
    image = models.ImageField(upload_to='post_image', blank=True, null=True)
    content = HTMLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = "Post"
 
    def __unicode__(self):
        return self.title