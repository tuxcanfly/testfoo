from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, CreateView

from bar.models import Poll, Avatar

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.all()),
        name='bar.index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll),
        name='bar.detail'),
    url(r'^avatar/$',
        ListView.as_view(
            queryset=Avatar.objects.all()),
        name='bar.index.avatar'),
    url(r'^avatar/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Avatar),
        name='bar.detail.avatar'),
    url(r'new/$',
        CreateView.as_view(
            model=Poll),
        name='bar.new'),
    url(r'new/avatar/$',
        CreateView.as_view(
            model=Avatar,
            success_url='/'),
        name='bar.new.avatar'),
)
