from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',), }


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
