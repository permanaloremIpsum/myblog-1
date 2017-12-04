# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from article.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'category', 'created_on', 'last_modified', 'user',
        'tagimage')
    list_filter = ('user', 'category')
    search_fields = ('title', )

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.user = request.user
    #     obj.slug = slugify(obj.title)
    #     super(PostAdmin, self).save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
