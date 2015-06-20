from django.conf.urls import include, url
from django.contrib import admin
import views


urlpatterns = [
    url(r'^logout/$', views.LogOutView.as_view(), name='logout'),
    url(r'^signin/$', views.SignInFormView.as_view(), name='signin'),
]
