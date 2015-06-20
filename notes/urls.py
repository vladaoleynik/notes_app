from django.conf.urls import include, url
from django.contrib import admin
from notes import views


urlpatterns = [
    url(r'^notes/$', views.IndexView.as_view(), name='index'),
    url(r'^notes/my_notes/$', views.MyNotesView.as_view(), name='my_notes'),
    url(r'^author/(?P<username>\w+)/$', views.NotesAuthorView.as_view(), name='notes_author'),
    url(r'^notes/category/(?P<category>\w+)/$', views.NotesCategoryView.as_view(), name='notes_category'),
    url(r'^notes/tag/(?P<tag>\w+)/$', views.NotesTagView.as_view(), name='notes_tag'),
]
