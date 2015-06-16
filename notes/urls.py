from django.conf.urls import include, url
from django.contrib import admin
from notes import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
