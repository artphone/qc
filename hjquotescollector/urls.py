from django.conf.urls import url, include
from django.contrib import admin
from hjquotescollector import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results')
]
