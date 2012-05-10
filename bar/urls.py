from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from bar.models import Poll

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.all()),
        name='bar.index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll),
        name='bar.detail'),
)
