from rest_framework import generics
from rest_data.serializers import NoteSerializer, CategorySerializer, TagSerializer, \
    UserSerializer, ColorSerializer, SettingsSerializer
from notes.models import Note, Category, Tag, Color, UserSettings
from django.contrib.auth.models import User
from rest_framework import permissions
import json
from django.core import serializers

"""
Notes api. Full notes list and note add.
"""


class NoteListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        return queryset

"""
Getting notes by author.
"""


class AuthorNoteListApi(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        queryset = Note.objects.filter(user__username=username)
        return queryset

"""
Getting, delete and edit note by id.
"""


class NoteApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Note.objects.filter(pk=pk)
        return queryset

"""
Getting list of notes by category.
"""


class NoteCategoryListApi(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        category = self.kwargs.get('category')
        queryset = Note.objects.filter(category__category__icontains=category)
        return queryset

"""
Getting list of notes by tag.
"""


class NoteTagListApi(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        queryset = Note.objects.filter(tag__tag__icontains=tag)
        return queryset

"""
Categories api. Full category list and add.
"""


class CategoryListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


"""
Tags api. Full tag list and add.
"""


class TagListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset


"""
Colors api. Full color list.
"""


class ColorListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ColorSerializer

    def get_queryset(self):
        queryset = Color.objects.all()
        return queryset

"""
Add user
"""


class UserApi(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

"""
Delete user
"""


class UserDeleteApi(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

"""
UserSettings
"""


class UserSettingsListApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SettingsSerializer
    lookup_field = 'user'

    def get_queryset(self):
        username = self.kwargs.get(self.lookup_field)
        queryset = UserSettings.objects.get(user__username=username)
        return queryset
