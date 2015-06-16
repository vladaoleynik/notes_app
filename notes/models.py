from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=6)


class Tag(models.Model):
    tag = models.CharField(max_length=40)


class Category(models.Model):
    category = models.CharField(max_length=40)


class UserSetting(models.Model):
    user = models.OneToOneField(User)
    id_color = models.ManyToManyField(Color, blank=True)
    id_tag = models.ManyToManyField(Tag, blank=True)
    id_category = models.ManyToManyField(Category, blank=True)


class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40)
    text = models.TextField()
    media = models.FileField(blank=True)
    id_color = models.OneToOneField(Color)
    id_tag = models.ManyToManyField(Tag, blank=True)
    id_category = models.ManyToManyField(Category)