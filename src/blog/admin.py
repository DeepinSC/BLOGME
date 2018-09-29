# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


# Register your models here.
admin.site.register(Blog, BlogAdmin)
