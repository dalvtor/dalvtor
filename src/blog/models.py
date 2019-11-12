from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _
from core.models import ModelBase


class Post(ModelBase):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    summary = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        db_table = 'post'
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(ModelBase):
    label = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = 'tag'
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super().save(*args, **kwargs)

