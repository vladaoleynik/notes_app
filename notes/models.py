from django.db import models
from django.contrib.auth.models import User


class Color(models.Model):
    color = models.CharField(max_length=6)
    status = models.CharField(default='user', max_length=10)

    def __unicode__(self):
        return '{0} - {1}'.format(self.color, self.status)


class Tag(models.Model):
    tag = models.CharField(max_length=40)
    status = models.CharField(default='user', max_length=10)

    def __unicode__(self):
        return '{0} - {1}'.format(self.tag, self.status)


class Category(models.Model):
    category = models.CharField(max_length=40)
    status = models.CharField(default='user', max_length=10)

    def __unicode__(self):
        return '{0} - {1}'.format(self.category, self.status)


class UserSettings(models.Model):
    user = models.OneToOneField(User)
    color = models.ManyToManyField(Color, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.user.username


class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40)
    text = models.TextField()
    media = models.FileField(blank=True, null=True)
    color = models.ForeignKey(Color)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)

    class Meta:
        permissions = (
            ("view_notes", "Anyone can see my notes"),
        )

    def __unicode__(self):
        return '{0} - {1}'.format(self.user.username, self.title)