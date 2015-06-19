__author__ = 'vladaoleynik'

from django.conf.urls import include, url
from rest_data import views


urlpatterns = [
    url(r'^notes/$', views.NoteListApi.as_view()),
    url(r'^notes/(?P<username>\w+)/$', views.AuthorNoteListApi.as_view()),
    url(r'^notes/(?P<username>\w+)/(?P<note_id>\d+)/$', views.NoteApi.as_view()),
]

