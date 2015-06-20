from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView, RetrieveDestroyAPIView
from rest_data.serializers import NoteSerializer, CategorySerializer, TagSerializer, \
    UserSerializer
from notes.models import Note, Category, Tag, SYSTEM_COLORS
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response


"""
Notes api. Full notes list and note add.
"""


class NoteListApi(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        return queryset

"""
Getting notes by author.
"""


class AuthorNoteListApi(ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.filter(user__username=self.kwargs.get('username'))
        return queryset

"""
Getting, delete and edit note by id.
"""


class NoteApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.filter(pk=self.kwargs.get('pk'))
        return queryset

"""
Getting list of notes by category.
"""


class NoteCategoryListApi(ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.filter(category__category__icontains=self.kwargs.get('category'))
        return queryset

"""
Getting list of notes by tag.
"""


class NoteTagListApi(ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.filter(tag__tag__icontains=self.kwargs.get('tag'))
        return queryset

"""
Categories api. Full category list and add.
"""


class CategoryListApi(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

"""
Categories get and delete.
"""


class CategoryDeleteApi(RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

"""
Tags api. Full tag list and add.
"""


class TagListApi(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset

"""
Tags get and delete.
"""


class TagDeleteApi(RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset

"""
Colors api. Full color list.
"""


class ColorListApi(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return Response(SYSTEM_COLORS)

"""
Add user
"""


class UserApi(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

"""
Delete user
"""


class UserDeleteApi(RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset