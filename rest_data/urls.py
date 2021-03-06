__author__ = 'vladaoleynik'

from django.conf.urls import include, url
from rest_data import views

notes_urls = [
    url(r'^$', views.NoteListApi.as_view()),
    url(r'^author/(?P<username>\w+)/$', views.AuthorNoteListApi.as_view()),
    url(r'^(?P<pk>\d+)/$', views.NoteApi.as_view()),
    url(r'^cat/(?P<category>\w+)/$', views.NoteCategoryListApi.as_view()),
    url(r'^tag/(?P<tag>\w+)/$', views.NoteTagListApi.as_view())
]

user_urls = [
    url(r'^$', views.UserApi.as_view()),
    url(r'^(?P<pk>\d+)/delete/$', views.UserDeleteApi.as_view()),
    url(r'^(?P<user>\w+)/tag/$', views.UserTagsListApi.as_view()),
    url(r'^(?P<user>\w+)/category/$', views.UserCategoriesListApi.as_view()),
    url(r'^(?P<user>\w+)/color/$', views.UserColorsListApi.as_view())
]


urlpatterns = [
    url(r'^notes/', include(notes_urls)),
    url(r'^category/$', views.CategoryListApi.as_view()),
    url(r'^color/$', views.ColorListApi.as_view()),
    url(r'^tag/$', views.TagListApi.as_view()),
    url(r'^user/', include(user_urls))
]