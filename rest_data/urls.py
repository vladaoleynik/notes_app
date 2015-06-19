__author__ = 'vladaoleynik'

from django.conf.urls import include, url
from rest_data import views


urlpatterns = [
    url(r'^notes/$', views.NoteListApi.as_view()),
    url(r'^notes/author/(?P<username>\w+)/$', views.AuthorNoteListApi.as_view()),
    url(r'^notes/(?P<pk>\d+)/$', views.NoteApi.as_view()),
    url(r'^notes/cat/(?P<category>\w+)/$', views.NoteCategoryListApi.as_view()),
    url(r'^notes/tag/(?P<tag>\w+)/$', views.NoteTagListApi.as_view()),
    url(r'^categories/$', views.CategoryListApi.as_view()),
    url(r'^categories/(?P<pk>\d+)/delete/$', views.CategoryDeleteApi.as_view()),
    url(r'^colors/$', views.ColorListApi.as_view()),
]

