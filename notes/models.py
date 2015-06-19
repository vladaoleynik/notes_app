from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=6, default='000000')

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


class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40)
    text = models.TextField()
    media = models.FileField(blank=True, null=True)
    color = models.ForeignKey(Color)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category)

    class Meta:
        permissions = (
            ("view_notes", "Anyone can see my notes"),
        )

    def __unicode__(self):
        return '{0} - {1}'.format(self.user.username, self.title)