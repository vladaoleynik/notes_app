from django.db import models
from django.contrib.auth.models import User
from notes.config import DEFAULT_COLORS


# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=6, default=DEFAULT_COLORS)

    def __unicode__(self):
        return self.color


class Tag(models.Model):
    tag = models.CharField(max_length=40)

    def __unicode__(self):
        return self.tag


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __unicode__(self):
        return self.category


class UserSetting(models.Model):
    user = models.OneToOneField(User)
    color = models.ManyToManyField(Color, blank=True, default=DEFAULT_COLORS)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.user__username


class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40)
    text = models.TextField()
    media = models.FileField(blank=True)
    permission = models.BooleanField(default=True)
    color = models.OneToOneField(Color)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return '{0} - {1}'.format(self.user__username, self.title)