from rest_framework import generics
from rest_data.serializers import NoteSerializer, CategorySerializer, TagSerializer, \
    UserSerializer, ColorSerializer, SettingsSerializer
from models import Note, Category, Tag, Color, UserSettings
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
        queryset = Category.objects.filter(status=0)
        return queryset


class UserCategoriesListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer
    lookup_field = 'user'

    def get_queryset(self):
        username = self.kwargs.get(self.lookup_field)
        status = User.objects.values('pk').get(username=username)
        status = status['pk']
        user = Category.objects.filter(status=status)
        return user


class UserColorsListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ColorSerializer
    lookup_field = 'user'

    def get_queryset(self):
        username = self.kwargs.get(self.lookup_field)
        status = User.objects.values('pk').get(username=username)
        status = status['pk']
        user = Color.objects.filter(status=status)
        return user


"""
Tags api. Full tag list and add.
"""


class TagListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tag.objects.filter(status=0)
        return queryset


class UserTagsListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TagSerializer
    lookup_field = 'user'

    def get_queryset(self):
        username = self.kwargs.get(self.lookup_field)
        tag_status = User.objects.values('pk').get(username=username)
        tag_status = tag_status['pk']
        user = Tag.objects.filter(status=tag_status)
        return user


"""
Colors api. Full color list.
"""


class ColorListApi(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ColorSerializer

    def get_queryset(self):
        queryset = Color.objects.filter(status=0)
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

