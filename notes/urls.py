from django.conf.urls import include, url
from django.contrib import admin
from notes import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^profile/my_notes/$', views.MyNotesView.as_view(), name='my_notes'),
    url(r'^profile/my_categories/$', views.MyCategoriesView.as_view(), name='my_categories'),
    url(r'^profile/my_tags/$', views.MyTagsView.as_view(), name='my_tags'),
    url(r'^profile/my_colors/$', views.MyColorsView.as_view(), name='my_colors'),
    url(r'^new_note/$', views.CreateNoteView.as_view(), name='new_note'),
    url(r'^note/(?P<pk>\d+)/$', views.ChangeNoteView.as_view(), name='single_note'),
    url(r'^note/(?P<pk>\d+)/delete/$', views.DeleteNoteView.as_view(), name='delete_note'),
    url(r'^author/(?P<username>\w+)/$', views.NotesAuthorView.as_view(), name='notes_author'),
    url(r'^notes/category/(?P<category>\w+)/$', views.NotesCategoryView.as_view(), name='notes_category'),
    url(r'^notes/tag/(?P<tag>\w+)/$', views.NotesTagView.as_view(), name='notes_tag')
]
